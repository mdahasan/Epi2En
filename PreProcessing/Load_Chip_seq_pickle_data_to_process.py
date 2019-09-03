"""
This code loads the pickles chip-seq data and process it into
input shape that fits into the model
"""

import pickle
import sys
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


def main():
    pickle_data_file = sys.argv[1]

    print "Reading pickle file..."
    start_time = time.time()
    list = process_pickled_file(pickle_data_file)
    end_time = time.time()
    print "Time to read pickle file: ", (end_time - start_time)

    print list[10075:10100]
    print list[10070:10105]
    print list[10100:10250]
    print list[10100:10255]

if __name__ == '__main__':
    main()
