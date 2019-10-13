import sys

"""
# Import files//Arguments
contig_file = open(sys.argv[1])
contig_file_lines = contig_file.readlines()
contig_interest = str(sys.argv[2])
start_position = int(sys.argv[3])
end_position = int(sys.argv[4])
"""

def make_contig_dict(contig_file_lines):
    # Put all of the contigs in a hash
    contig_dict = {}
    for line in contig_file_lines:
        if ">" in line:
            split_lines = line.split(" ")
            contig_name = split_lines[0].replace(">","")
            contig_dict[contig_name] = []
        else: 
            contig_dict[contig_name].append(line.strip().strip("\n"))

    for key in contig_dict.keys():
        contig_dict[key] = "".join(contig_dict[key])

    return contig_dict;

def contig_fixer(contig_dictionary, contig, start_posit, stop_posit, sv_type, contig_seq, real_seq):
    
    if sv_type == 'DEL': #This is really an insert
        # Find the sequence before and after the insertion
        contig_seq = contig_dictionary[contig]
        before_ins = contig_seq[:start_posit]
        after_ins = contig_seq[stop_posit:] ###REVISIT: make sure this is the right starting indexx!!

        #make a new contig sequence
        new_contig = [before_ins, real_seq, after_ins]
        new_contig = "".join(new_contig)
        contig_dictionary[contig] = new_contig

        #return the updated contig dictionary
        return contig_dictionary;

    if sv_type == 'INS': #This is really a deletion
        # Find the sequence before and after the deletion
        contig_seq = contig_dictionary[contig]
        before_del = contig_seq[:start_posit]
        after_del = contig_seq[stop_posit:]

        #make a new contig sequence
        new_contig = [before_del, real_seq, after_del]
        new_contig = "".join(new_contig)
        contig_dictionary[contig] = new_contig

        #return the updated dictionary
        return contig_dictionary;

    if sv_type == 'INV': #This is an inversion
        # Find the sequence before and after the inversion
        contig_seq = contig_dictionary[contig]
        before_inv = contig_seq[:start_posit]
        after_inv = contig_seq[stop_posit:]

        #make a new contig sequence
        new_contig = [before_inv, real_seq, after_inv]
        new_contig = "".join(new_contig)
        contig_dictionary[contig] = new_contig

        #return the updated dictionary
        return contig_dictionary;


# The below was used for testing
"""
contig_dict = make_contig_dict();

#contig_dict = contig_fixer(contig_dict, 'unk325', 15162, 15184, 'DEL', 'ATATATATATATATATATAT','A')

#unk325 15398   MantaINS:63:0:0:0:0:1   T       TAAAAAATTTTTTATATAA     .       .       END=15398;
#contig_dict = contig_fixer(contig_dict, 'unk325', 15398, 15398, 'INS', 'T', 'TAAAAAATTTTTTATATAA')

#contig_dict = contig_fixer(contig_dict, 'unk325', 15398, 15398, 'INS', 'T', 'TAAAAAATTTTTTATATAA')

contig_dict = contig_fixer(contig_dict, 'unk325', 15398, 15398, 'INV', 'TTTTCCCC', 'CCCCTTTT')

# Pull out region of interest from the contig
print (contig_dict[contig_interest][start_position:end_position])

print ( len(contig_dict[contig_interest]))

"""
