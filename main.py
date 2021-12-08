from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline

import os

records = []
for filename in os.scandir("./unaligned"):
    records.append(SeqIO.parse(filename, "fasta"))
        
#Write filtered data to file
SeqIO.write(records, "all_unaligned.fasta", "fasta")
#Align sequences with MUSCLE (using parameters to make the alignment
#process as fast as possible)
muscle_cline = MuscleCommandline(input="all_unaligned.fasta", 
                                 out="all_aligned.fasta", 
                                 diags = True, 
                                 maxiters = 1)
muscle_cline()

## code taken from https://towardsdatascience.com/introduction-to-sequence-alignments-with-biopython-f3b6375095db