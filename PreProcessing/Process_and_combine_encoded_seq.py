"""
This codes takes in the enhancer/non-enhancer one hot encoded sequence and combine them into
one file. This code may also split the data into smaller dataset
"""

import sys
import pickle
import random
import os
import glob


def process_pickled_file(pickle_file):
    infile = open(pickle_file, 'rb')
    return_dict = pickle.load(infile)
    infile.close()

    return return_dict


def pickle_data(D, file_name):
    filename = str(file_name)
    outfile = open(filename, 'wb')
    pickle.dump(D, outfile)
    outfile.close()


def main():
    sequence_dir = sys.argv[1]          # directory containing all one-hot-encoded sequences
    cell_line_name = sys.argv[2]        # name of the cell line

    os.chdir(sequence_dir)

    enhancer_sample_size = random.randint(5000, 6000)
    non_enhancer_sample_size = enhancer_sample_size * 10

    sub_encoded_enhancer_seq_dict = dict()
    sub_encoded_nonenhancer_seq_dict = dict()

    for file in glob.glob("*.pkl"):
        if cell_line_name in file and "_enhancer_" in file:
            print file
            enhancer_coded_seq_dict = process_pickled_file(file)

            print len(enhancer_coded_seq_dict)

            all_keys = enhancer_coded_seq_dict.keys()
            random_keys = random.sample(list(all_keys), enhancer_sample_size)
            sub_encoded_enhancer_seq_dict = dict()
            for i in range(len(random_keys)):
                sub_encoded_enhancer_seq_dict[random_keys[i]] = (enhancer_coded_seq_dict[random_keys[i]], 1)

        if cell_line_name in file and "_nonenhancer_" in file:
            print file
            nonenhancer_coded_seq_dict = process_pickled_file(file)

            all_keys = nonenhancer_coded_seq_dict.keys()
            random_keys = random.sample(list(all_keys), non_enhancer_sample_size)
            sub_encoded_nonenhancer_seq_dict = dict()
            for i in range(len(random_keys)):
                sub_encoded_nonenhancer_seq_dict[random_keys[i]] = (nonenhancer_coded_seq_dict[random_keys[i]], 0)

    cell_line_dict = sub_encoded_enhancer_seq_dict.copy()
    cell_line_dict.update(sub_encoded_nonenhancer_seq_dict)

    file_name = str(cell_line_name) + '_200bp_' + str(enhancer_sample_size) + '_e_' + str(non_enhancer_sample_size) + '_ne_encoded_seq_dataset.pkl'
    pickle_data(cell_line_dict, file_name)

if __name__ == '__main__':
    main()
