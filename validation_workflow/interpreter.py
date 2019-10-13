import sys
import fasta_parser as fp
import vcf_parser as vp


# Import files//Arguments
input_vcf = str(sys.argv[1])
contig_file = open(sys.argv[2])
contig_file_lines = contig_file.readlines()
output_file = str(sys.argv[3])

# Making the datastructure with the vcf info
vcf_df = vp.parse_vcf(input_vcf)

# Fixing the contigs
contig_dict = fp.make_contig_dict(contig_file_lines);
for struct_var in range(0,len(vcf_df.loc[:,'Contig Name'])):
    # Iterating through information in the vcf
    contig_name = vcf_df.loc[struct_var,'Contig Name']
    start_position = vcf_df.loc[struct_var,'SV POS']
    stop_position = vcf_df.loc[struct_var,'SV STOP']
    ref_seq = vcf_df.loc[struct_var,'REF SV']
    read_seq = vcf_df.loc[struct_var,'ALT SV']
    sv_type = vcf_df.loc[struct_var,'SV type']

    #print statement for updating user
    print ("Updating contig " + str(contig_name))

    # Fixing the contigs
    contig_dict = fp.contig_fixer(contig_dict, contig_name, start_position, stop_position, sv_type, ref_seq, read_seq)

# Save the updated contigs into a new fasta file
out_file = open (output_file, "a+")
for contig in contig_dict.keys():
    out_file.write(">" + contig + "\n")
    out_file.write(contig_dict[contig] + "\n")
