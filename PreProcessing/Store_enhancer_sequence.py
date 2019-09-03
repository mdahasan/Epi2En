"""
3.1. This code search and stores the correpsonding genomic sequence
of the enhancer regions
"""

import sys
from Bio import SeqIO


def main():
    fasta_file = sys.argv[1]                # cell line specific enhancer fasta file
    enhancer_file = sys.argv[2]             # enhancer range bed file

    cell_line = fasta_file.split('.')[0]

    chr1_enhancer_positions = list()
    chr1_enhancer_sequence_dict = dict()

    chr2_enhancer_positions = list()
    chr2_enhancer_sequence_dict = dict()

    chr3_enhancer_positions = list()
    chr3_enhancer_sequence_dict = dict()

    chr4_enhancer_positions = list()
    chr4_enhancer_sequence_dict = dict()

    chr5_enhancer_positions = list()
    chr5_enhancer_sequence_dict = dict()

    chr6_enhancer_positions = list()
    chr6_enhancer_sequence_dict = dict()

    chr7_enhancer_positions = list()
    chr7_enhancer_sequence_dict = dict()

    chr8_enhancer_positions = list()
    chr8_enhancer_sequence_dict = dict()

    chr9_enhancer_positions = list()
    chr9_enhancer_sequence_dict = dict()

    chr10_enhancer_positions = list()
    chr10_enhancer_sequence_dict = dict()

    ##

    chr11_enhancer_positions = list()
    chr11_enhancer_sequence_dict = dict()

    chr12_enhancer_positions = list()
    chr12_enhancer_sequence_dict = dict()

    chr13_enhancer_positions = list()
    chr13_enhancer_sequence_dict = dict()

    chr14_enhancer_positions = list()
    chr14_enhancer_sequence_dict = dict()

    chr15_enhancer_positions = list()
    chr15_enhancer_sequence_dict = dict()

    chr16_enhancer_positions = list()
    chr16_enhancer_sequence_dict = dict()

    chr17_enhancer_positions = list()
    chr17_enhancer_sequence_dict = dict()

    chr18_enhancer_positions = list()
    chr18_enhancer_sequence_dict = dict()

    chr19_enhancer_positions = list()
    chr19_enhancer_sequence_dict = dict()

    chr20_enhancer_positions = list()
    chr20_enhancer_sequence_dict = dict()

    chr21_enhancer_positions = list()
    chr21_enhancer_sequence_dict = dict()

    chr22_enhancer_positions = list()
    chr22_enhancer_sequence_dict = dict()

    chrX_enhancer_positions = list()
    chrX_enhancer_sequence_dict = dict()

    fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)

        chromosome = name.split(':')[0]
        rest_name = name.split(':')[1]
        only_positions = rest_name.split('_')[0]
        start_pos = int(only_positions.split('-')[0])
        end_pos = int(only_positions.split('-')[1])

        if chromosome == 'chr1':
            chr1_enhancer_positions.append((start_pos, end_pos))
            chr1_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr2':
            chr2_enhancer_positions.append((start_pos, end_pos))
            chr2_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr3':
            chr3_enhancer_positions.append((start_pos, end_pos))
            chr3_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr4':
            chr4_enhancer_positions.append((start_pos, end_pos))
            chr4_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr5':
            chr5_enhancer_positions.append((start_pos, end_pos))
            chr5_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr6':
            chr6_enhancer_positions.append((start_pos, end_pos))
            chr6_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr7':
            chr7_enhancer_positions.append((start_pos, end_pos))
            chr7_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr8':
            chr8_enhancer_positions.append((start_pos, end_pos))
            chr8_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr9':
            chr9_enhancer_positions.append((start_pos, end_pos))
            chr9_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr10':
            chr10_enhancer_positions.append((start_pos, end_pos))
            chr10_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        ##

        if chromosome == 'chr11':
            chr11_enhancer_positions.append((start_pos, end_pos))
            chr11_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr12':
            chr12_enhancer_positions.append((start_pos, end_pos))
            chr12_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr13':
            chr13_enhancer_positions.append((start_pos, end_pos))
            chr13_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr14':
            chr14_enhancer_positions.append((start_pos, end_pos))
            chr14_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr15':
            chr15_enhancer_positions.append((start_pos, end_pos))
            chr15_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr16':
            chr16_enhancer_positions.append((start_pos, end_pos))
            chr16_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr17':
            chr17_enhancer_positions.append((start_pos, end_pos))
            chr17_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr18':
            chr18_enhancer_positions.append((start_pos, end_pos))
            chr18_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr19':
            chr19_enhancer_positions.append((start_pos, end_pos))
            chr19_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr20':
            chr20_enhancer_positions.append((start_pos, end_pos))
            chr20_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr21':
            chr21_enhancer_positions.append((start_pos, end_pos))
            chr21_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chr22':
            chr22_enhancer_positions.append((start_pos, end_pos))
            chr22_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

        if chromosome == 'chrX':
            chrX_enhancer_positions.append((start_pos, end_pos))
            chrX_enhancer_sequence_dict[(start_pos, end_pos)] = sequence

    file_name = str(cell_line) + '.enseq'
    fopen = open(file_name, 'w')

    # process enhancer file
    with open(enhancer_file, 'r') as ef:
        for line in ef.readlines():
            line = line.strip()
            cols = line.split()

            enhancer_start = int(cols[1])
            enhancer_end = int(cols[2])

            if cols[0] == 'chr1':
                for i in range(len(chr1_enhancer_positions)):
                    seq_start = chr1_enhancer_positions[i][0]
                    seq_end = chr1_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr1_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr2':
                for i in range(len(chr2_enhancer_positions)):
                    seq_start = chr2_enhancer_positions[i][0]
                    seq_end = chr2_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr2_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr3':
                for i in range(len(chr3_enhancer_positions)):
                    seq_start = chr3_enhancer_positions[i][0]
                    seq_end = chr3_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr3_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr4':
                for i in range(len(chr4_enhancer_positions)):
                    seq_start = chr4_enhancer_positions[i][0]
                    seq_end = chr4_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr4_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr5':
                for i in range(len(chr5_enhancer_positions)):
                    seq_start = chr5_enhancer_positions[i][0]
                    seq_end = chr5_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr5_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr6':
                for i in range(len(chr6_enhancer_positions)):
                    seq_start = chr6_enhancer_positions[i][0]
                    seq_end = chr6_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr6_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr7':
                for i in range(len(chr7_enhancer_positions)):
                    seq_start = chr7_enhancer_positions[i][0]
                    seq_end = chr7_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr7_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr8':
                for i in range(len(chr8_enhancer_positions)):
                    seq_start = chr8_enhancer_positions[i][0]
                    seq_end = chr8_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr8_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr9':
                for i in range(len(chr9_enhancer_positions)):
                    seq_start = chr9_enhancer_positions[i][0]
                    seq_end = chr9_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr9_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr10':
                for i in range(len(chr10_enhancer_positions)):
                    seq_start = chr10_enhancer_positions[i][0]
                    seq_end = chr10_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr10_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            ##

            if cols[0] == 'chr11':
                for i in range(len(chr11_enhancer_positions)):
                    seq_start = chr11_enhancer_positions[i][0]
                    seq_end = chr11_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr11_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr12':
                for i in range(len(chr12_enhancer_positions)):
                    seq_start = chr12_enhancer_positions[i][0]
                    seq_end = chr12_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr12_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr13':
                for i in range(len(chr13_enhancer_positions)):
                    seq_start = chr13_enhancer_positions[i][0]
                    seq_end = chr13_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr13_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr14':
                for i in range(len(chr14_enhancer_positions)):
                    seq_start = chr14_enhancer_positions[i][0]
                    seq_end = chr14_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr14_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr15':
                for i in range(len(chr15_enhancer_positions)):
                    seq_start = chr15_enhancer_positions[i][0]
                    seq_end = chr15_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr15_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr16':
                for i in range(len(chr16_enhancer_positions)):
                    seq_start = chr16_enhancer_positions[i][0]
                    seq_end = chr16_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr16_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr17':
                for i in range(len(chr17_enhancer_positions)):
                    seq_start = chr17_enhancer_positions[i][0]
                    seq_end = chr17_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr17_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr18':
                for i in range(len(chr18_enhancer_positions)):
                    seq_start = chr18_enhancer_positions[i][0]
                    seq_end = chr18_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr18_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr19':
                for i in range(len(chr19_enhancer_positions)):
                    seq_start = chr19_enhancer_positions[i][0]
                    seq_end = chr19_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr19_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr20':
                for i in range(len(chr20_enhancer_positions)):
                    seq_start = chr20_enhancer_positions[i][0]
                    seq_end = chr20_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr20_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr21':
                for i in range(len(chr21_enhancer_positions)):
                    seq_start = chr21_enhancer_positions[i][0]
                    seq_end = chr21_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr21_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chr22':
                for i in range(len(chr22_enhancer_positions)):
                    seq_start = chr22_enhancer_positions[i][0]
                    seq_end = chr22_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chr22_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')

            if cols[0] == 'chrX':
                for i in range(len(chrX_enhancer_positions)):
                    seq_start = chrX_enhancer_positions[i][0]
                    seq_end = chrX_enhancer_positions[i][1]

                    if seq_start <= enhancer_start <= enhancer_end <= seq_end:
                        enhancer_seq_start = enhancer_start - seq_start
                        enhancer_seq = chrX_enhancer_sequence_dict[(seq_start, seq_end)]
                        selected_enhancer_seq = enhancer_seq[enhancer_seq_start:enhancer_end]
                        fopen.write(str(cols[0]) + '\t' + str(enhancer_start) + '\t' + str(enhancer_end) + '\t' +
                                    selected_enhancer_seq + '\n')


if __name__ == '__main__':
    main()
