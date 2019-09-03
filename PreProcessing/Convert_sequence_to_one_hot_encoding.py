"""
This code takes input as enhancer/non-enhancer sequence and convert
the sequence into a binary one-hot-encoding matrix.
The size of the matrix is matched with the largest sequence by padding
zeros as the end
"""

import sys
import numpy as np
import glob
import os
import pickle


def process_to_one_hot_encode(seq, max_length):

    encoded_matrix = np.zeros((max_length, 4), dtype = int)
    for i in range(len(seq)):
        if seq[i] in 'Aa':
            encoded_matrix[i, 0] = 1
        elif seq[i] in 'Cc':
            encoded_matrix[i, 1] = 1
        elif seq[i] in 'Gg':
            encoded_matrix[i, 2] = 1
        elif seq[i] in 'Tt':
            encoded_matrix[i, 3] = 1

    return encoded_matrix


def pickle_data(D, file_name):
    filename = str(file_name)
    outfile = open(filename, 'wb')
    pickle.dump(D, outfile)
    outfile.close()


def main():
    seq_dir = sys.argv[1]

    os.chdir(seq_dir)

    print "Check for enhancer/non-enhancer file extension..."

    for file in glob.glob("*.nenseq"):
        cell_line = file.split('.')[0]

        print cell_line

        seq_lengths = list()

        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                cols = line.split('\t')

                sequence = cols[3]
                seq_lengths.append(len(sequence))

        max_seq_length = max(seq_lengths)
        encoded_sequence_dict = dict()

        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                cols = line.split('\t')

                chromosome = cols[0]
                start_pos = cols[1]
                end_pos = cols[2]

                sequence = cols[3]

                encoded_seq = process_to_one_hot_encode(sequence, max_seq_length)

                key = str(chromosome) + '_' + str(start_pos) + '_' + str(end_pos)
                encoded_sequence_dict[key] = encoded_seq

        for key in encoded_sequence_dict:
            print key, encoded_sequence_dict[key]
            break

        file_name = str(cell_line) + '_nonenhancer_one_hot_encodings.pkl'
        pickle_data(encoded_sequence_dict, file_name)


if __name__ == '__main__':
    main()

