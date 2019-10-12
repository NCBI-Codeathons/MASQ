# MASQ

## Abstract
Metagenomic assembly is an important technique to reconstruct organisms by stitching together gene sequences. A major concern is that detected structural variants or SNPS could actually be the results of misassembled data instead of actual biological phenomena. Our goal is to identify errors in metagenomic assembly creation based on short and long sequencing reads in the hopes of eliminating some of the uncertainty in metagenomic studies. Examples of errors are: inversions, chimeras (translocation), indels (<50bp), replacements (large substitutions). We are creating a containerized quality control pipeline called MASQ.

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

![Random Forest](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/NCBI_hackathon.jpg)
A random forest classifier will be used to elucidate the type of each assembly error that is detected by the MASQ pipeline. 

Visualization of the detected assembly errors will be carried out through IGV.
## Key Results
This will be updated after project completion.


## Discussion 

### Future Directions
+ Test by running on simulated data
+ Use a more sophisticated classifier model
+ Could combine a detection model with the classifier

### Reproduction
#### Docker
![Docker screenshot](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/docker_ncbi.png)

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
