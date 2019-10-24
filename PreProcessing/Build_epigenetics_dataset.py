"""
This code combines enhance and non-enhancer pickle file and store the
epigenetics matrices in a list of pairs. The pair contains the epigentics
matix for each sample and label. 1 - enhancer, 0 - non-enhancer
"""

import sys
import pickle
import os
import glob
import time
import random
import numpy as np


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


def process_to_one_hot_encode(seq):

    encoded_matrix = np.zeros((len(seq), 4), dtype = int)
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


def store_sample_matrix_in_list(sample_dict, class_label):
    sample_matrices_in_list = list()
    for sample_id in sample_dict:
        sample_info_pair = (sample_dict[sample_id], class_label)
        sample_matrices_in_list.append(sample_info_pair)

    return sample_matrices_in_list

def main():
    cell_line_epi_dir = sys.argv[1]

    cell_line = cell_line_epi_dir.split('/')[-2]
    print cell_line

    start_time = time.time()

    ###### Process and store the enhancer epigenetics signals ##########
    print
    print "Start processing the " + str(cell_line) + " enhancer epigenetics data..."
    os.chdir(cell_line_epi_dir)

    enhancer_epi_list = list()
    enhancer_region_list = list()

    for file in glob.glob("*.pkl"):
        selected_enhancer_epi_list = list()
        selected_enhancer_epi_region_list = list()
        if "_10_binned_enhancers_" in file:
            print "Started reading Enhancer file..."
            print file
            feature_to_skip = file.split('.')[0].split('_')[-2]
            print feature_to_skip
            enhancer_epi_dict = process_pickled_file(file)
            print "Enhancer file reading done"

            for sample in enhancer_epi_dict:
                selected_enhancer_epi_list.append((enhancer_epi_dict[sample], 1))
                selected_enhancer_epi_region_list.append((sample, 1))

        enhancer_epi_list.extend(selected_enhancer_epi_list)
        enhancer_region_list.extend(selected_enhancer_epi_region_list)

    print "Enhancer epigenetics data processing done."
    print "Size of enhancer data: ", len(enhancer_epi_list)

    # selecting the size of the dataset. Can be changed
    num_of_enhancers = int(len(enhancer_epi_list) * 1)
    num_of_nonenhancers = num_of_enhancers * 10                 # size of nonenhancers are 10 times enhancers

    print
    print "Size of the enhancers to be selected: ", num_of_enhancers
    print "Size of the non-enhancers to be selected: ", num_of_nonenhancers
    print
    ####### Process and store the non-enhancer epigeentics signals ###########
    print
    print "Start processing the " + str(cell_line) + " non-enhancer epigenetics data..."
    os.chdir(cell_line_epi_dir)
    nonenhancer_epi_list = list()
    nonenhancer_epi_region_list = list()

    for file in glob.glob("*.pkl"):
        selected_non_enhancer_epi_list = list()
        selected_non_enhancer_epi_region_list = list()
        if "_10_binned_nonenhancers_" in file:
            print "Started reading Non-Enhancer file..."
            print file
            nonenhancer_epi_dict = process_pickled_file(file)
            print "Non-Enhancer file reading done"

            for sample in nonenhancer_epi_dict:
                selected_non_enhancer_epi_list.append((nonenhancer_epi_dict[sample], 0))
                selected_non_enhancer_epi_region_list.append((sample, 0))

        nonenhancer_epi_list.extend(selected_non_enhancer_epi_list)
        nonenhancer_epi_region_list.extend(selected_non_enhancer_epi_region_list)

        if len(nonenhancer_epi_list) > num_of_nonenhancers:
            break

    print "Non-Enhancer epigenetics data processing done."
    print "Size of non-enhancer data: ", len(nonenhancer_epi_list)

    print
    print "Combining enhancer and non-enhancer dataset..."
    combined_epi_list = enhancer_epi_list + nonenhancer_epi_list
    combined_epi_region_list = enhancer_region_list + nonenhancer_epi_region_list

    epi_file_name = str(cell_line) + '_binned_' + str(num_of_enhancers) + '_e_' + str(num_of_nonenhancers) + '_ne_epi_dataset' + '.pkl'
    epi_region_file_name = str(cell_line) + '_binned_' + str(num_of_enhancers) + '_e_' + str(num_of_nonenhancers) + '_ne_epi_regions' + '.pkl'

    print "Pickle Epigenetics dataset..."
    pickle_data(combined_epi_list, epi_file_name)

    print "Pickle Epigenetics dataset regions..."
    pickle_data(combined_epi_region_list, epi_region_file_name)

    end_time = time.time()
    print "Total time required to build datasets: ", (end_time - start_time)


if __name__ == '__main__':
    main()
