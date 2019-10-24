"""
This code process the pre-processed dataset and build the
dataset suitable for the deep learning model
"""

import pickle
import random
import numpy as np
import time
from sklearn.preprocessing import StandardScaler


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


# returns scaled training dataset
def getScaledData(dataMatrix):
    scaler = StandardScaler().fit(dataMatrix)
    return scaler.transform(dataMatrix)


def check_matrix_shape(epi_matrix):
    good_matrix = False

    # print len(epi_matrix)

    if not len(epi_matrix) == 12:
        return good_matrix

    for row in range(0, len(epi_matrix)):
        # print len(epi_matrix[row])
        if len(epi_matrix[row]) == 10:
            good_matrix = True
        else:
            good_matrix = False
            # print len(epi_matrix[row])
            break

    return good_matrix


def reshape_matrix(matrix):
    row, col = matrix[0].shape
    reshaped_sample_index = 0
    reshaped_matrix = np.zeros((len(matrix), row, col), dtype = float)
    # this is to check if every sample has same lenght of histone marks signals
    for sample_id in range(len(matrix)):
        for i in range(row):
            for j in range(col):
                reshaped_matrix[reshaped_sample_index, i, j] = float(matrix[sample_id][i][j])
        reshaped_sample_index += 1

    return reshaped_matrix


def reshape_list(list):
    reshaped_list = np.zeros((len(list), 1), dtype = int)
    for sample_id in range(len(list)):
        reshaped_list[sample_id] = list[sample_id]

    return reshaped_list


class DataProcessing(object):
    def __init__(self, *argv):
        super(DataProcessing, self).__init__()

        self.epidata_file = argv[0]
        self.region_file = argv[1]

    def get_epi_dataset(self):
        return process_epi_dataset(self.epidata_file, self.region_file)

    # def get_sequence_dataset(self):
    #     return process_sequence_dataset(self.seqdata_file)


def process_epi_dataset(epidata_file, region_file=None, non_enh_size = 1):
    start_time = time.time()
    print "Reading epigenetics data..."
    epi_data_in_pair_list = process_pickled_file(epidata_file)  # this returns a list of pairs, first element is a matrix of
    # epi signals and the second value is the class label, 1 (enh) 0 (non-enh)
    print "Reading epigenetics data done."
    end_time = time.time()
    print "Time needed to read epigenetics info: ", (end_time - start_time)

    epi_region_pair_list = process_pickled_file(region_file)
    #
    c = zip(epi_data_in_pair_list, epi_region_pair_list)
    random.shuffle(c)
    epi_region_pair_list, epi_region_pair_list = zip(*c)

    # random.shuffle(epi_data_in_pair_list)       # randomly shuffle the dataset before splitting into training/testing

    sample_epi_matrices = list()
    sample_epi_regions = list()
    sample_labels = list()

    print "Total initial sample count: ", len(epi_data_in_pair_list)
    bad_enhancer_sample_count = 0
    bad_non_enhancer_sample_count = 0

    for i in range(len(epi_data_in_pair_list)):
        if check_matrix_shape(epi_data_in_pair_list[i][0]):
            sample_epi_matrices.append(np.array(epi_data_in_pair_list[i][0]))
            sample_epi_regions.append(epi_region_pair_list[i][0])
            sample_labels.append(epi_data_in_pair_list[i][1])
        else:
            if epi_data_in_pair_list[i][1] == 1:
                bad_enhancer_sample_count += 1
            else:
                bad_non_enhancer_sample_count += 1

    print "Number of bad enhancer samples: ", bad_enhancer_sample_count
    print "Number of bad non-enhancer samples: ", bad_non_enhancer_sample_count
    print "Remaining number of samples: ", len(sample_epi_matrices), len(sample_labels)

    print
    print "Size of initial dataset: ", len(sample_epi_matrices)
    print "Percentage of non-enhancer: ", non_enh_size

    reshaped_sample_epi_matrices = reshape_matrix(sample_epi_matrices)
    reshaped_sample_labels = reshape_list(sample_labels)

    epi_dataset = {
        'reshaped_sample_matrices': reshaped_sample_epi_matrices,
        'reshaped_sample_labels': reshaped_sample_labels,

        'sample_matrices': sample_epi_matrices,
        'sample_labels': sample_labels,
        'sample_region': sample_epi_regions,
    }

    return epi_dataset


def process_sequence_dataset(seq_file):
    start_time = time.time()
    print "Reading encoded sequence data..."
    seq_data_in_pair_list = process_pickled_file(seq_file)      # this returns a dictionary of pairs, first element is the encoded
    #   sequence and the second value is the class label, 1 (enh), 0 (non-enh)
    print "Reading encoded sequence file done."
    end_time = time.time()

    print "Time needed to read encoded sequence info: ", (end_time - start_time)

    random.shuffle(seq_data_in_pair_list)

    sample_encoded_seq_matrices = list()
    sample_labels = list()

    for i in range(len(seq_data_in_pair_list)):
        sample_encoded_seq_matrices.append(np.transpose(np.array(seq_data_in_pair_list[i][0])))
        sample_labels.append(seq_data_in_pair_list[i][1])




    reshaped_sample_encoded_seq_matrices = reshape_matrix(sample_encoded_seq_matrices)
    reshaped_sample_labels = reshape_list(sample_labels)

    seq_dataset = {
        'sample_matrices': reshaped_sample_encoded_seq_matrices,
        'sample_labels': reshaped_sample_labels
    }

    return seq_dataset
