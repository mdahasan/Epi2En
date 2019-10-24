"""
4. This code takes in all the histone modification files with epigenetics
signals and combine then into one file. Each enhancer/non-enhancer is
represented by epi signals are formatted in a matrix format and stored
"""

import sys
import glob
import os
import math
import numpy as np
import pickle
import random
import time


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


def process_epi_signals_by_binning(signal_list, bin_size):

    number_of_signals_in_bins = int(math.ceil(len(signal_list)/bin_size))
    new_sample_list_size = number_of_signals_in_bins * bin_size
    signal_list = signal_list[0:new_sample_list_size]
    # print len(signal_list)

    binned_epi_signals = list()
    start = 0
    end = number_of_signals_in_bins
    while end <= len(signal_list):
        if end - start == number_of_signals_in_bins:
            binned_epi_signals.append(np.mean(signal_list[start:end]))
        start = end
        end = end + number_of_signals_in_bins

    # print len(binned_epi_signals)
    return binned_epi_signals


def process_epi_signals_by_padding(signal_list, max_enh_length):
    while len(signal_list) < max_enh_length:
        signal_list.append(0.0)

    return signal_list


def main():
    cell_line_dir = sys.argv[1]
    bin_size = sys.argv[2]              # bin size: 10

    start_time = time.time()

    os.chdir(cell_line_dir)

    ####################################### Enhancer processing ########################################################
    cell_line_dict = dict()
    binned_cell_line_dict = dict()
    cell_line_name = ""

    # process enhancer files and store in a pickle file
    print "Processing enhancer files..."
    for file in glob.glob("*.enh"):
        method_name = (file.split('.')[0]).split('_')[0]
        cell_line_name = (file.split('.')[0]).split('_')[1]

        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                cols = line.split('\t')

                chromosome = cols[0]
                start_pos = cols[1]
                end_pos = cols[2]

                key = str(chromosome) + '_' + str(start_pos) + '_' + str(end_pos)

                if len(cols[3:]) > 0:
                    binned_epi_signals = process_epi_signals_by_binning([float(x) for x in cols[3:]], int(bin_size))
                    epi_signals = [float(x) for x in cols[3:]]

                    # to check if each histone mark has entry for the region
                    if len(epi_signals) > 0:
                        if key in binned_cell_line_dict:
                            binned_cell_line_dict[key].append(binned_epi_signals)
                            cell_line_dict[key].append(epi_signals)
                        else:
                            binned_cell_line_dict[key] = [binned_epi_signals]
                            cell_line_dict[key] = [epi_signals]

    print "Total enhancer: ", len(binned_cell_line_dict), len(binned_cell_line_dict[key])

    total_enhancer = len(binned_cell_line_dict)
    enhancer_count = 0
    file_count = 1
    binned_sub_cell_line_dict = dict()

    for key in binned_cell_line_dict:
        binned_sub_cell_line_dict[key] = binned_cell_line_dict[key]
        enhancer_count += 1

        if (enhancer_count % 50000) == 0 or enhancer_count == total_enhancer:
            print enhancer_count, total_enhancer
            file_name_binned = str(method_name) + '_' + str(cell_line_name) + '_' + str(bin_size) + '_binned_enhancers_epi_signals_' + str(file_count) + '.pkl'
            print "Pickle sub sample enhancer epi signal dictionary..."
            pickle_data(binned_cell_line_dict, file_name_binned)

            binned_sub_cell_line_dict.clear()
            file_count += 1

    ####################################### Non-enhancer processing ########################################################
    # process non-enhancer files and store in a pickle file
    cell_line_dict = dict()
    binned_cell_line_dict = dict()

    # These are predetermined number for given cell-lines, will change for new cell-lines #
    print cell_line_name
    if cell_line_name == "H1":             # ******* absolutely need to change ******** #
        total_non_enhancer = 90000         # pre-determined for GM12878
    if cell_line_name == "HepG2":
        total_non_enhancer = 140000
    if cell_line_name == "Huvec":
        total_non_enhancer = 330000
    if cell_line_name == "Gm12878":
        total_non_enhancer = 193000
    if cell_line_name == "Hela":
        total_non_enhancer = 190000
    if cell_line_name == "K562":
        total_non_enhancer = 180000

    print "Processing non-enhancer files..."
    for file in glob.glob("*.nenh"):
        line_count = 0
        method_name = (file.split('.')[0]).split('_')[0]
        cell_line_name = (file.split('.')[0]).split('_')[1]

        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                cols = line.split('\t')

                chromosome = cols[0]
                start_pos = cols[1]
                end_pos = cols[2]

                key = str(chromosome) + '_' + str(start_pos) + '_' + str(end_pos)

                if len(cols[3:]) > 100:
                    binned_epi_signals = process_epi_signals_by_binning([float(x) for x in cols[3:]], int(bin_size))
                    epi_signals = [float(x) for x in cols[3:]]

                    # to check if each histone mark has entry for the region
                    if len(epi_signals) > 0:
                        if key in binned_cell_line_dict:
                            binned_cell_line_dict[key].append(binned_epi_signals)
                            cell_line_dict[key].append(epi_signals)
                        else:
                            binned_cell_line_dict[key] = [binned_epi_signals]
                            cell_line_dict[key] = [epi_signals]

                    if line_count == total_non_enhancer:
                        break
                    line_count += 1

    print "Total Non-enhancer: ", len(binned_cell_line_dict)

    total_non_enhancer = len(binned_cell_line_dict)
    non_enhancer_count = 0
    file_count = 1
    binned_sub_cell_line_dict = dict()
    # padded_sub_cell_line_dict = dict()

    for key in binned_cell_line_dict:
        binned_sub_cell_line_dict[key] = binned_cell_line_dict[key]
        non_enhancer_count += 1

        if (non_enhancer_count%50000) == 0 or non_enhancer_count == total_non_enhancer:
            print non_enhancer_count, total_non_enhancer
            file_name_binned = str(method_name) + '_' + str(cell_line_name) + '_' + str(bin_size) + '_binned_nonenhancers_epi_signals_' + str(file_count) + '.pkl'
            print "Pickle sub sample nonenhancer epi signal dictionary..."
            pickle_data(binned_sub_cell_line_dict, file_name_binned)

            binned_sub_cell_line_dict.clear()

            file_count += 1

    end_time = time.time()
    print "Time required for the process: ", (end_time - start_time)


if __name__ == '__main__':
    main()
