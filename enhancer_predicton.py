#### enhancer practice ####
# This project is to practice predicting enhancer sequences
# using refGene.txt, ChIA-PET data, and DNase-seq data
# Author: Ha-Eun Hwangbo
# Date: 2017/07/10

HumanChrList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y']

class Promoter:
	def __init__ (self, tokens):
		""" parses refGene.txt file to obtain necessary fields.
		caller should check for coding/noncoding and haplotype.

		Args:
			line (string): refGene.txt line

		refGene.txt header fields
		0 `bin` smallint(5) unsigned NOT NULL,
		1 `name` varchar(255) NOT NULL,
		2 `chrom` varchar(255) NOT NULL,
		3 `strand` char(1) NOT NULL,
		4 `txStart` int(10) unsigned NOT NULL,
		5 `txEnd` int(10) unsigned NOT NULL,
		...
		""" 
		self.name = tokens[1]
		self.chr = int(tokens[2][3:])
		self.strand = tokens[3]

		tss = 0
		if self.strand == "+":
			tss = int(tokens[4])
		elif self.strand == "-":
			tss = int(tokens[5])
		else
			print("Error: invalid strand info")
			return

		self.start = tss - 1000

	def parse_refGene(self, tokes):

		self.end = tss + 1000
	### END - refGene

	def name(self):
		return self.name

	def start(self):
		return self.start

	def end(self):
		return self.end


class DHS:
	def __init__(self, tokens):
		""" parses DHS peak bed file.
		file format:
		chr#	start 	end 	peakname	score
		chr1	10084	10085	NA_peak_1	22.52676
		"""

		self.chr = tokens[0][3:]
		self.start = int(tokens[1])
		self.end = int(tokens[2])


class ChIA-PET


def check_validity(tokens):
	if tokens[1][:2] != "NM":
		return False

	if tokens[2][3:] not in HumanChrList:
		return False

	return True