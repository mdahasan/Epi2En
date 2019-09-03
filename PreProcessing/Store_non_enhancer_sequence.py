"""
3.2. This code reads the hg19 fasta sequence and then extract corresponding
non-enhancer sequence and store
"""

import sys
from Bio import SeqIO

def main():
    fasta_file = sys.argv[1]            # hg19 fasta file
    non_enhancer_file = sys.argv[2]

    cell_line = ((non_enhancer_file.split('/')[-1]).split('.')[0]).split('_')[0]
    print cell_line

    genome_dict = dict()

    fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)

        if len(name) < 7:
            genome_dict[name] = sequence

    f_non_enhancer_seq = open(str(cell_line) + '.nenseq', 'w')
    with open(non_enhancer_file) as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            chromosome = cols[0]
            non_enhancer_start = int(cols[1])
            non_enhancer_end = int(cols[2])

            seq = genome_dict[chromosome][non_enhancer_start:non_enhancer_end]

            f_non_enhancer_seq.write(str(chromosome) + '\t' + str(non_enhancer_start) + '\t' + str(non_enhancer_end) + '\t' +
                                     str(seq) + '\n')

    f_non_enhancer_seq.close()


if __name__ == '__main__':
    main()
