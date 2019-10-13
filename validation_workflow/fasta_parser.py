import sys

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

