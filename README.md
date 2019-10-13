# MASQ
![masklogo](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/mask_logo.jpg)

## Abstract
While metagenomic assembly has significantly improved since the early days of the Human Microbiome Project (HMP), it remains confounded by intragenomic and intergenomic repetitive sequences. Individual reads that span microbial strains (either via long read technology or clever techniques for generating synthetic long reads) to fully resolve variation within a given community. Recent benchmarking studies on error rates in metagenomic assembly range between 1 and 10 major SV error per MB of assembled sequenced. Thus major concern is that detected structural variants could actually result from misassembled data instead of actual strain specific variation. This goal of this project is to identify errors in metagenomic assembly based on short and long read mapping, in the hope of eliminating some of the uncertainty and error in metagenomic studies. Examples of errors we are MASQing are: inversions, chimeras (translocation), indels (<50bp), replacements (large substitutions). We are creating a containerized quality control pipeline called MASQ.

## Getting Started
*how to run the pipeline*

## Methods
![NCBIpipeline](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/Updated%20Pipeline.png)

### Datasets
+ Zymobiomics Microbial Community Standards Assemblies (10 genomes; 5 gram positive, 3 gram negative, 2 yeast)
  + Short reads 
  (http://ftp-private.ncbi.nlm.nih.gov/nist-immsa/IMMSA/)
  (https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1299-7#MOESM2)
  + Long reads 
  + Has a known reference
+ Shakya Assembly (using MegaHIT and MetaSPAdes)
  + Short reads
  + Has a known reference

### Data collection and initial processing
downloaded fastq files, ran fastqc to check the quality of the sequencing reads -> good to go!
used megahit and metaspades to build assemblies from the zymo and shakya datasets

### Secondary processing

### Pre-tertiary processing


### Machine Learning Model to Classify Assembly Errors
![Random Forest](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/NCBI_hackathon.jpg)
A random forest classifier will be used to classify the type of each assembly error that is detected by the MASQ pipeline. 
*briefly explain what a random forest is and how it will be used to extract imp features and make predictions*
*can use scikit-learn package for Python*

## Key Results
This will be updated after project completion.

*Visualization of the detected assembly errors will be carried out through IGV.*
*insert labeled/captioned figures showing example assembly errors here*

## Discussion 
### Future Directions
+ Test by running on simulated data
+ Use a more sophisticated classifier model
+ Once imp features are identified, could integrate a detection model alongside the classifier model (?)

### Reproduction
#### Docker
![Docker screenshot](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/NCBI_pipeline (1).png)

#### DNA Nexus
![DNANexuspipeline](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/image.png)

## Contributors
+ Todd Treangen 
+ Michael Jochum
+ Adam English
+ Shakuntala Mitra
+ Junzhou Wang
+ Yongze Yin
+ Advait Balaji
+ Dreycey Albin
