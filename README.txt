This program generates psuedo mRNA sequences(nucleotide sequences) without affecting the inherent frequency of the nucleotides in the original sequence. It randomly shuffles the synonymous codons present in the original mRNA sequences without affecting the original amino-acid sequences. 

1. test.txt sequence is used in codon_separation_on_AA_basis.py for the generation of codoncount.txt file.

2.codoncount.txt and pep.txt(amino-acid sequence) file of the original mRNA is used in randomisation.py to create the psuedo random mRNA with the same number of codons and nucleotide frequency in the original file. 