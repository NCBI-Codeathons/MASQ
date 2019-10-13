# Validation Workflow
## Author: Dreycey Albin

## Dependencies

For the validation workflow, the dependencies are samtools and pandas. Samtools is used to parse the vcf files and pandas is used to save this information into a dataframe. 

### How to download dependencies:

* For pandas
``` pip install pandas ```

* For samtools
``` conda install -c bioconda samtools ```


## Workflow

The master file interpreter.py calls on below workflows, vcf_parser.py and fasta_parser.py, which process the vcf files and edit the contigs with the needed changes, respectively. 

