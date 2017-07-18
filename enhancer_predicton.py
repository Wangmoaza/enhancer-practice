#### enhancer practice ####
# This project is to practice predicting enhancer sequences
# using refGene.txt, ChIA-PET data, and DNase-seq data
# Author: Ha-Eun Hwangbo
# Date: 2017/07/18

import pandas as pd
import numpy as np
import re

def get_data(dhs_file, chip_file, refGene_file):
	""" Convert data files to desired data frames.
		args:
			dhs_file (string): path to DHS narrowPeak file
			chip_file (string): path to chIP-seq bed file
			refGene_file (string): path to refGene.txt

		returns:
			tuple of dhs, chip, promoter data frames
	"""


	# convert dhs narrowPeak file to pandas dataframe
	# format: chrom / start / end
	dhs = pd.read_table(dhs_file, sep='\t', header=None, index_col=False,
                         names=['chrom', 'start', 'end','name', 'score', 'strand', 'signalValue', 'pValue', 'qValue', 'peak'])
	dhs.drop(['signalValue', 'pValue', 'qValue', 'strand', 'name', 'score', 'peak'], axis=1, inplace=True)
	dhs = dhs.apply(pd.to_numeric, errors='ignore')

	# convert chIP-seq bed file to pandas dataframe
	# format: chrom1 / start1 / end1 / chrom2 / start2 / end2 / score
	chip = pd.read_table(chip_file, sep='\t', header=None, index_col=False,
                     names=['chrom', 'start', 'end', 'interaction', 'score', 'strand', 'unknown', 'unknown2', 'itemRGB', 'unknown3', 'length'])
	chip.drop(['score', 'strand', 'unknown', 'unknown2', 'itemRGB', 'unknown3', 'length'], axis=1, inplace=True)
	groups = "(?P<chrom1>chr\w+)[:](?P<start1>\d+)(..)(?P<end1>\d+)[-](?P<chrom2>chr\w+)[:](?P<start2>\d+)(..)(?P<end2>\d+)[,](?P<score>\d+)"
	chip = chip['interaction'].str.extract(groups, expand=True)
	chip.drop([2, 6], axis=1, inplace=True)  # remove (..) columns
	chip.drop_duplicates(inplace=True)
	chip = chip.apply(pd.to_numeric, errors='ignore')

	# convert refGene.txt file to pandas dataframe
	# format: name / chrom / strand / promStart / promEnd
	refGene = pd.read_table(refGene_file, sep='\t', header=None, index_col=False,
                         names=['bin', 'name', 'chrom', 'strand', 'txStart', 'txEnd'] + range(10))
	refGene.drop(['bin'] + range(10), axis=1, inplace=True) # drop unnecessary columns
	refGene.drop(refGene[refGene.name.str.startswith('NR_')].index, axis=0, inplace=True)  # drop noncoding genes
	# drop haplotype genes
	pattern = 'chr\w+[_]\w+'
	refGene.drop(refGene[refGene.chrom.str.contains(pattern)].index, axis=0, inplace=True)

	# make promoter data frame
	prom = []
	for idx, row in refGene.iterrows():
		if row.strand == '-':
			prom.append(row.txEnd)
		elif row.strand == '+':
			prom.append(row.txStart)
	### END - for
	prom = np.asarray(prom)
	promoter = pd.DataFrame({'promStart': prom - 1000, 'promEnd': prom + 1000}, index=refGene.index)
	promoter = pd.concat([refGene, promoter], axis=1)
	promoter.drop(['txStart', 'txEnd'], axis=1, inplace=True)

	# sort by gene names and drop genes that have same promoters (keep the least numbered gene)
	# FIXME should I delete genes that have overlapping promoters?
	promoter.sort_values('name', axis=0, inplace=True)
	promoter.drop_duplicates(subset=['promEnd', 'promStart'], inplace=True)

	promoter = promoter[['name', 'chrom', 'strand', 'promStart', 'promEnd']] # reorder columns
	print "*** importing file DONE ***"
	return dhs, chip, promoter
### END - get_data

def match(dhs, chip, promoter):
	""" match promoter-chip-dhs to make data frame of promoter-enhancer interaction
	args:
		dhs (pandas DataFrame): dhs data frame
		chip (pandas DataFrame): chip-seq data frame
		promoter (pandas DataFrame): prmoter information data frame

	returns:
		resulting promoter-interaction DataFrame
	"""
	out_arr = np.empty((0, 8), dtype=object) # value ndarray for matchedProm data frame
	for chipIdx, chipRow in chip.iterrows():
		# match promoter to chip
		# consider as matched if overlapped even by 1 base
		condition1 = (promoter.chrom == chipRow.chrom1) & (promoter.promEnd > chipRow.start1) & (promoter.promStart < chipRow.end1)
		condition2 = (promoter.chrom == chipRow.chrom2) & (promoter.promEnd > chipRow.start2) & (promoter.promStart < chipRow.end2)
		tmp_df1 = promoter[condition1]
		tmp_df2 = promoter[condition2]

		# np ndarray of values, fill empty tmp_out array with elements
		m1, m2 = tmp_df1.shape[0], tmp_df2.shape[0] 
		r = promoter.shape[1]
		tmp_out = np.empty((m1+m2,r+3),dtype=object)
		# matched with first seq block
		tmp_out[:m1, :r] = tmp_df1.values[:, :]
		tmp_out[:m1, r:r+3] = np.array([chipRow.start2, chipRow.end2])
		# matched with second seq block
		tmp_out[m1:m1+m2, :r] = tmp_df2.values[:, :]
		tmp_out[m1:m1+m2, r:r+3] = np.array([chipRow.start1, chipRow.end1])
		# stack output array
		out_arr = np.vstack((out_arr, tmp_out))
	### END - for
	print "*** matching promoter to chip DONE ***"
	matchedProm = pd.DataFrame(out_arr, columns=['name', 'chrom', 'strand', 'promStart', 'promEnd', 'enChrom', 'enStart', 'enEnd'])

	# remove promoter-promoter interaction
	for promIdx, promRow in promoter.iterrows():
		isPromoter = (promRow.chrom == matchedProm.enChrom) & (promRow.promEnd > matchedProm.enStart) & (promRow.promStart < matchedProm.enEnd)
		matchedProm = matchedProm.drop(matchedProm[isPromoter].index)
	### END - for
	print "*** removing promoter-promoter interaction DONE ***"

	# match dhs to matchedProm
	result_arr = np.empty((0, 8), dtype=object)
	for dhsIdx, dhsRow in dhs.iterrows():
		condition = (dhsRow.chrom == matchedProm.enChrom) & (dhsRow.end > matchedProm.enStart) & (dhsRow.start < matchedProm.enEnd)
		tmp_df = matchedProm[condition]
		m, r = tmp_df.shape[0], matchedProm.shape[1]
		tmp_out = np.empty((m, r), dtype=object)
		# change chip-seq value to dhs start end value
		tmp_out[:, :-2] = tmp_df.values[:, :-2]
		tmp_out[:, -2:] = dhsRow.values[-2:]
		result_arr = np.vstack((result_arr, tmp_out))
	### END - for
	print "*** matching dhs to matchedProm DONE"
	result = pd.DataFrame(result_arr, columns=['name', 'chrom', 'strand', 'promStart', 'promEnd', 'enChrom', 'enStart', 'enEnd'])
	return result
### END - match

def main():
	dhs, chip, promoter = get_data("../NA_peaks.narrowPeak", "../wgEncodeGisChiaPetK562Pol2InteractionsRep1.bed", "../refGene.txt")
	result = match(dhs, chip, promoter)
	result.to_csv('promoter-enhancer.csv')

if __name__ == "__main__":
	main()