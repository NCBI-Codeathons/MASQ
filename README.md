# MASQ
![masklogo](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/mask_logo.jpg)

## Abstract
While metagenomic assembly has significantly improved since the early days of the Human Microbiome Project (HMP), it remains confounded by intragenomic and intergenomic repetitive sequences. Individual reads that span microbial strains (either via long read technology or clever techniques for generating synthetic long reads) to fully resolve variation within a given community. Recent benchmarking studies on error rates in metagenomic assembly range between 1 and 10 major SV error per MB of assembled sequenced. Thus major concern is that detected structural variants could actually result from misassembled data instead of actual strain specific variation. This goal of this project is to identify errors in metagenomic assembly based on short and long read mapping, in the hope of eliminating some of the uncertainty and error in metagenomic studies. Examples of errors we are MASQing are: inversions, chimeras (translocation), indels (<50bp), replacements (large substitutions). We are creating a containerized quality control pipeline called MASQ.

## Getting Started
MasQ uses Python 3.x. 
Download requirements from here.

## Methods
![NCBIpipeline](https://github.com/NCBI-Codeathons/MASQ/blob/master/workflow10.13.png)

### Datasets
+ Zymobiomics Microbial Community Standards Assemblies (10 genomes; 5 gram positive, 3 gram negative, 2 yeast)
  + Has a known reference
  + Synthetic bacteria included: Bacillus subtilis, Cryptococcus neoformans, Enterococcus faecalis, Escherichia coli, Lactobacillus fermentum, Listeria monocytogenes, Pseudomonas aeruginosa, Saccharomyces cerevisiae, Salmonella enterica, Staphylococcus aureus
  + Illumina pair-ended short reads from [IMMSA dataset](http://ftp-private.ncbi.nlm.nih.gov/nist-immsa/IMMSA/) 
  + Sequencing depth:
  + Average read length:
  + Oxford Nanopore long reads
  + Sequencing depth: 
  + Average read length: 
  
+ Shakya Assembly (assembled using MegaHIT and MetaSPAdes)
  + Has a known reference
  + Synthetic bacteria included: Acidobacterium capsulatum, aciduliprofundum boonei, akkermansia muciniphila, archaeoglobus fulgidus, Bacteroides thetaiotaomicron, Bacteroides vulgatus, Bordetella bronchiseptica, Burkholderia xenovorans LB400, Caldicellulosiruptor bescii, Caldicellulosiruptor saccharolyticus, Chlorobium limicola, Chlorobium phaeobacteroides, Chlorobium phaeovibriodes, Chlorobium tepidum, Chloroflexus aurantiacus, Clostridium thermocellum, Deinococcus radiodurans, Desulfovibrio piger, Desulfovibrio vulgaris, Dictyoglomus turgidum, Enterococcus faecalis, Fusobacterium nucleatum, Gemmatimonas aurantiacus, Geobacter sulfurreducens, Haloferax volcanii, Herpetosiphon aurantiacus, Hydrogenobaculum, Ignicoccus hospitalis, Leptothrix cholodnii, Methanocaldococcus jannaschii, Methanococcus maripaludis C5, Methanococcus maripaludis S2, Methanopyrus kandleri, Methanosarcina acetivorans C2A, Nanoarchaeum equitans, Nitrosomonas europaea, Nostoc sp. PCC 7120, Pelodictyon phaeoclatharatiforme, Persephonella marina EX-H1, Porphyromonas gingivalis, Pyrobaculum aerophilum IM2, Pyrobaculum arsenaticum, Pyrobaculum calidifontis, Pyrococcus furiosus, Pyrococcus horikoshii, Rhodopirellula baltica, Ruegeria pomeroyi, Salinispora arenicola, Salinispora tropica, Shewanella baltica OS185, Shewanella baltica OS223, Sulfitobacter sp.EE-36, Sulfitobacter sp.NAS-14.1, Sulfolobus tokodaii, Sulfurihydrogenibium sp.YO3AOP1, Sulfurihydrogenibium yellowstonense, Thermoanaerobacter pseudethanolicus, Thermotoga neapolitana DSM 4359, Thermotoga petrophila RKU-1, Thermotoga sp.RQ2, Thermus thermophilus HB8, Treponema denticola, Zymomonas mobilis
  + From Illumina pair-ended short reads 
  + Sequencing depth:
  + Number of sequences: 54814748
  + Read length: 101bp

### Data collection and initial processing
downloaded fastq files, ran fastqc to check the quality of the sequencing reads -> good to go!
used megahit and metaspades to build assemblies from long and short reads

### Assembly

### Classification

### Correction

### Validation

## Key Results

The MasQ pipeline can smoothly and successfully locate assembly errors. Some examples (visualized with IGV) are shown below:

Inversion:
![Inversion Example]()

Insertion:
![Insertion Example](https://github.com/NCBI-Codeathons/MASQ/blob/master/figures/k119_12877_51-222_inse_igv_snapshot.png)

Deletion:
![Deletion Example](https://github.com/NCBI-Codeathons/MASQ/blob/master/figures/igv_snapshot_k119_18959_del.png)

The MasQ pipeline detected an insertion (labeled Unk570) in the Zymo long read assembly, which is shown by the section of very low mapped reads in IGV. 
![Unk570](https://github.com/NCBI-Codeathons/MASQ/blob/master/figures/unk570_igv_snapshot.png)

This is an example of an assembly error that MasQ will fix during the correction step. The validation script checks the percentage of mapped reads in the corrected assembly and shows a ______ increase in mapped reads from the original assembly. Thus, MasQ was successful in correcting assembly errors.

Here we can see the corrected assembly mapping of the same locus (previously Unk570) visualized with IGV
*insert picture once finished running*

## Discussion 
### Future Directions
+ Test by running on simulated data
+ Use a machine learning model such as random forest, SVM, or CNN to classify types of assembly errors
#### Machine Learning Model to Classify Assembly Errors
![Random Forest](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/NCBI_hackathon.jpg)
A random forest classifier could be used to classify the type of each assembly error that is detected by the MASQ pipeline. 
*briefly explain what a random forest is and how it will be used to extract imp features and make predictions*
*can use scikit-learn package for Python*
Other options for classification models are SVM (Support Vector Machine) or CNN (Convolutional Neural Network).


### Reproduction
#### Docker
The MasQ pipeline is freely available for download and use on DockerHub.
![Docker screenshot](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/docker_ncbi.png)

#### DNA Nexus
[How to run workflow in DNA Nexus](https://documentation.dnanexus.com/developer/workflows/building-and-running-workflows)

Once all of the inputs for all of the apps in the workflow have been satisfied (indicated by the black app box showing a green runnable label instead of orange set inputs), you can run the workflow by clicking on the green Start Analysis button in the upper right of the workflow.

![DNANexuspipeline](https://github.com/NCBI-Codeathons/Meta_QC/blob/master/figures/image.png)

#### Implementation 
[All relevant parameters can be found documented here.](https://github.com/NCBI-Codeathons/MASQ/blob/master/implementation.md)

## Contributors
+ Todd Treangen 
+ Michael Jochum
+ Adam English
+ Shakuntala Mitra
+ Junzhou Wang
+ Yongze Yin
+ Advait Balaji
+ Dreycey Albin
