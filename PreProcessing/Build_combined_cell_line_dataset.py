"""
This code combines all the datasets except one. The (n-1) dataset
is the training set and the rest one is the testing
"""

import sys
import os
import pickle


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
    pickled_dataset_dir = sys.argv[1]

    os.chdir(pickled_dataset_dir)

    files = [
        # 'DEEP_GM12878_no_promoter_binned_19362_e_193620_ne_epi_dataset.pkl',
        # 'DEEP_H1_no_promoter_binned_8098_e_80980_ne_epi_dataset.pkl',
        # 'DEEP_Hep_no_promoter_binned_13977_e_139770_ne_epi_dataset.pkl',
        'PEDLA_GM12878_binned_8579_e_85790_ne_epi_dataset.pkl',
        'PEDLA_H1_binned_5870_e_58700_ne_epi_dataset.pkl',
        'PEDLA_Hep_binned_8953_e_89530_ne_epi_dataset.pkl'
    ]

    GM12878 = process_pickled_file(files[0])
    print "GM12878 done..."
    print len(GM12878)
    H1 = process_pickled_file(files[1])
    print "H1 done..."
    print len(H1)
    Hep = process_pickled_file(files[2])
    print "Hep done..."
    print len(Hep)
    # Huvec = process_pickled_file(files[3])
    # print "Huvec done..."
    # print len(Huvec)


    list1 = GM12878 + H1 + Hep
    print len(list1)
    # list2 = Hep + H1
    # print len(list2)
    # list3 = GM12878 + Hep
    # print (len(list3))


    pickle_data(list1, 'PEDLA_GM12878_H1_Hep.pkl')
    print "Pickle list 1 done..."
    # pickle_data(list2, 'PEDLA_H1_Hep.pkl')
    # print "Pickle list 2 done..."
    # pickle_data(list3, 'PEDLA_GM12878_Hep.pkl')
    # print "Pickle list 3 done..."
    # pickle_data(list4, 'H1_Hep_Huvec.pkl')
    # print "Pickle list 4 done..."

if __name__ == '__main__':
    main()
