# Lab note for enhancer practice session

This project is to practice utilizing DNase-seq, ChIA-PET, and refGene files. I used these three files to get a list of promoter-enhancer interactions.


The epigenomic data used here are frome the ENCODE project.
* DNase-seq : DNaseI Hypersensitivity by Digital DNaseI from ENCODE/University of Washington. K562 Cell Line. Downloaded from [here](http://hgdownload.soe.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeUwDnase/wgEncodeUwDnaseK562RawDataRep1.fastq.gz)
* ChIA-PET : Chromatin Interaction Analysis Paired-End Tags (ChIA-PET) from ENCODE/GIS-Ruan. K562 Cell Line. Downloded from [here](http://hgdownload.soe.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeGisChiaPet/wgEncodeGisChiaPetK562Pol2InteractionsRep1.bed.gz)
* refGene.txt: hg19. Downloaded from [here](http://hgdownload.soe.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz)

I obtained promoter position from refGene.txt using txStart (+ strand) and txEnd (- strand). Promoter was defined as +- 1000bp from TSS.

### 2017-07-17
* parsing data using pandas pandas library
* doing tutorials


### 2017-07-18
* dhs, chip-seq, refGene data conversion to pandas data frame - DONE.
* finished first draft.
* error raised during execution. need to debug tomorrow.


### 2017-07-19
* FIXME should I remove chip row that overlaps?
* FIXME should I delete genes that have overlapping promoters?
* except implementing the above two, executed enhancer_prediction.py
* enhancer_prediction - DONE

[primer3](1) : construct initial primer sequence. surround must-include sequence with []
[Primer-BLAST](2) : check if primer aligns to other sequences
[Addgene](3) : find vector sequence. pSTARR-seq-human
[In-fusion primer](4) : convert PCR primers into in-fusion primer


~~bye bye~~

