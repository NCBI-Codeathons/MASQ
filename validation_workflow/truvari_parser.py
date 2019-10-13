import pysam
import sys


#Input files/flags
input_bam = sys.argv[1]

#Opening the bam
samfile = pysam.AlignmentFile(input_bam, "rb")

for read in samfile.fetch('chr1', 100, 120):
     print read

samfile.close()
