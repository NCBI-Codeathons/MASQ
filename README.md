# MASQ

## Abstract
Metagenomic assembly is an important technique to reconstruct organisms from their gene sequences. Our goal is to identify errors in metagenomic assembly creation based on short reads. Examples of errors are: inversions, chimeras (translocation), indels (<50bp), replacements (large substitutions). We are creating a containerized quality control pipeline called MASQ.

## Workflow
![Flowchart](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/workflow1.jpg)

## Methods
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

### Analysis pipeline
![NCBIpipeline](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/NCBI_pipeline%20(1).png)


## Key Results
This will be updated after project completion.


## Discussion 

### Future Directions
This will be updated after project completion.

### Reproduction
#### Docker

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
+ Dreycey
