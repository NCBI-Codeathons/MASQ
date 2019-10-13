from pysam import VariantFile
import sys
import pandas as pd

def parse_vcf(input_vcf):
    # Opening the input file
    vcf_in = VariantFile(input_vcf, 'r')  # auto-detect input format

    # making the different arrays
    contig_list = [i.contig for i in vcf_in.fetch()]
    sv_type_list = [i.info['SVTYPE'] for i in vcf_in.fetch()]
    sv_reference = [i.ref for i in vcf_in.fetch()]
    sv_alternative = [i.alts[0] for i in vcf_in.fetch()]
    sv_position = [i.pos for i in vcf_in.fetch()]
    sv_stop_pos = [i.stop for i in vcf_in.fetch()]

    # putting all of the relevant vcf information into a datastructure
    import pandas as pd 
      
    # intialize data of lists. 
    vcf_data = {'Contig Name':contig_list, 'SV type':sv_type_list, 'REF SV':sv_reference, 'ALT SV':sv_alternative, 'SV POS':sv_position, 'SV STOP':sv_stop_pos} 
    pandas_dataframe = pd.DataFrame(vcf_data)

    return pandas_dataframe;

#print(parse_vcf(sys.argv[1]))

