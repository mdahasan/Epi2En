"""
2. This code process the ChIP-seq signals from the bed file and
process them into one sequential file per chromosome

"""

import sys
import os
import pickle
import glob
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
    cell_line_dir = sys.argv[1]                 # directory of the cell line
    region_list_file = sys.argv[2]              # DEEP dataset training data
    class_type = sys.argv[3]                    # enh/nenh

    os.chdir(cell_line_dir)

    method_name = (region_list_file.split('/')[-1]).split('_')[0]
    print method_name

    for file in glob.glob('*.bed'):

        print(file)

        cell_line = (file.split('.')[0]).split('_')[0]
        histone_mark = (file.split('.')[0]).split('_')[1]

        chr1_epi_signals = list()
        chr2_epi_signals = list()
        chr3_epi_signals = list()
        chr4_epi_signals = list()
        chr5_epi_signals = list()
        chr6_epi_signals = list()
        chr7_epi_signals = list()
        chr8_epi_signals = list()
        chr9_epi_signals = list()
        chr10_epi_signals = list()
        chr11_epi_signals = list()
        chr12_epi_signals = list()
        chr13_epi_signals = list()
        chr14_epi_signals = list()
        chr15_epi_signals = list()
        chr16_epi_signals = list()
        chr17_epi_signals = list()
        chr18_epi_signals = list()
        chr19_epi_signals = list()
        chr20_epi_signals = list()
        chr21_epi_signals = list()
        chr22_epi_signals = list()
        chrX_epi_signals = list()

        print('Start reading ChIP-Seq bed file...')
        start_time = time.time()
        line_count = 0
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                cols = line.split('\t')

                start_pos = int(cols[1])
                end_pos = int(cols[2])
                signal = float(cols[3])

                if cols[0] == 'chr1':
                    if len(chr1_epi_signals) < start_pos:
                        for i in range(len(chr1_epi_signals), start_pos):
                            chr1_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr1_epi_signals.append(signal)

                if cols[0] == 'chr2':
                    if len(chr2_epi_signals) < start_pos:
                        for i in range(len(chr2_epi_signals), start_pos):
                            chr2_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr2_epi_signals.append(signal)

                if cols[0] == 'chr3':
                    if len(chr3_epi_signals) < start_pos:
                        for i in range(len(chr3_epi_signals), start_pos):
                            chr3_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr3_epi_signals.append(signal)

                if cols[0] == 'chr4':
                    if len(chr4_epi_signals) < start_pos:
                        for i in range(len(chr4_epi_signals), start_pos):
                            chr4_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr4_epi_signals.append(signal)

                if cols[0] == 'chr5':
                    if len(chr5_epi_signals) < start_pos:
                        for i in range(len(chr5_epi_signals), start_pos):
                            chr5_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr5_epi_signals.append(signal)

                if cols[0] == 'chr6':
                    if len(chr6_epi_signals) < start_pos:
                        for i in range(len(chr6_epi_signals), start_pos):
                            chr6_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr6_epi_signals.append(signal)

                if cols[0] == 'chr7':
                    if len(chr7_epi_signals) < start_pos:
                        for i in range(len(chr7_epi_signals), start_pos):
                            chr7_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr7_epi_signals.append(signal)

                if cols[0] == 'chr8':
                    if len(chr8_epi_signals) < start_pos:
                        for i in range(len(chr8_epi_signals), start_pos):
                            chr8_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr8_epi_signals.append(signal)

                if cols[0] == 'chr9':
                    if len(chr9_epi_signals) < start_pos:
                        for i in range(len(chr9_epi_signals), start_pos):
                            chr9_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr9_epi_signals.append(signal)

                if cols[0] == 'chr10':
                    if len(chr10_epi_signals) < start_pos:
                        for i in range(len(chr10_epi_signals), start_pos):
                            chr10_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr10_epi_signals.append(signal)


                ####

                if cols[0] == 'chr11':
                    if len(chr11_epi_signals) < start_pos:
                        for i in range(len(chr11_epi_signals), start_pos):
                            chr11_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr11_epi_signals.append(signal)

                if cols[0] == 'chr12':
                    if len(chr12_epi_signals) < start_pos:
                        for i in range(len(chr12_epi_signals), start_pos):
                            chr12_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr12_epi_signals.append(signal)

                if cols[0] == 'chr13':
                    if len(chr13_epi_signals) < start_pos:
                        for i in range(len(chr13_epi_signals), start_pos):
                            chr13_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr13_epi_signals.append(signal)

                if cols[0] == 'chr14':
                    if len(chr14_epi_signals) < start_pos:
                        for i in range(len(chr14_epi_signals), start_pos):
                            chr14_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr14_epi_signals.append(signal)

                if cols[0] == 'chr15':
                    if len(chr15_epi_signals) < start_pos:
                        for i in range(len(chr15_epi_signals), start_pos):
                            chr15_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr15_epi_signals.append(signal)

                if cols[0] == 'chr16':
                    if len(chr16_epi_signals) < start_pos:
                        for i in range(len(chr16_epi_signals), start_pos):
                            chr16_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr16_epi_signals.append(signal)

                if cols[0] == 'chr17':
                    if len(chr17_epi_signals) < start_pos:
                        for i in range(len(chr17_epi_signals), start_pos):
                            chr17_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr17_epi_signals.append(signal)

                if cols[0] == 'chr18':
                    if len(chr18_epi_signals) < start_pos:
                        for i in range(len(chr18_epi_signals), start_pos):
                            chr18_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr18_epi_signals.append(signal)

                if cols[0] == 'chr19':
                    if len(chr19_epi_signals) < start_pos:
                        for i in range(len(chr19_epi_signals), start_pos):
                            chr19_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr19_epi_signals.append(signal)

                if cols[0] == 'chr20':
                    if len(chr20_epi_signals) < start_pos:
                        for i in range(len(chr20_epi_signals), start_pos):
                            chr20_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr20_epi_signals.append(signal)

                if cols[0] == 'chr21':
                    if len(chr21_epi_signals) < start_pos:
                        for i in range(len(chr21_epi_signals), start_pos):
                            chr21_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr21_epi_signals.append(signal)

                if cols[0] == 'chr22':
                    if len(chr22_epi_signals) < start_pos:
                        for i in range(len(chr22_epi_signals), start_pos):
                            chr22_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chr22_epi_signals.append(signal)

                if cols[0] == 'chrX':
                    if len(chrX_epi_signals) < start_pos:
                        for i in range(len(chrX_epi_signals), start_pos):
                            chrX_epi_signals.append(0.0)

                    for i in range(start_pos, end_pos):
                        chrX_epi_signals.append(signal)

        # write corresponding histone signal for enhancer regions
        print "Building signal for " + str(histone_mark) + " histon marks for sample regions..."
        file_name = str(method_name) + '_' + str(cell_line) + '_' + str(histone_mark) + '.' + str(class_type)
        fopen = open(file_name, 'w')

        with open(region_list_file, 'r') as ef:
            for line in ef.readlines():
                line = line.strip()
                cols = line.split()

                if cols[0] == 'chr1':
                    signal_values = chr1_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr1' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr2':
                    signal_values = chr2_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr2' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr3':
                    signal_values = chr3_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr3' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr4':
                    signal_values = chr4_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr4' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr5':
                    signal_values = chr5_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr5' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr6':
                    signal_values = chr6_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr6' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr7':
                    signal_values = chr7_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr7' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr8':
                    signal_values = chr8_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr8' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr9':
                    signal_values = chr9_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr9' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr10':
                    signal_values = chr10_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr10' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                ###

                if cols[0] == 'chr11':
                    signal_values = chr11_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr11' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr12':
                    signal_values = chr12_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr12' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr13':
                    signal_values = chr13_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr13' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr14':
                    signal_values = chr14_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr14' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr15':
                    signal_values = chr15_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr15' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr16':
                    signal_values = chr16_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr16' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr17':
                    signal_values = chr17_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr17' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr18':
                    signal_values = chr18_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr18' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr19':
                    signal_values = chr19_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr19' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr20':
                    signal_values = chr20_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr20' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr21':
                    signal_values = chr21_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr21' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chr22':
                    signal_values = chr22_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chr22' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

                if cols[0] == 'chrX':
                    signal_values = chrX_epi_signals[int(cols[1]): int(cols[2])]
                    fopen.write('chrX' + '\t' + str(cols[1]) + '\t' + str(cols[2]) + '\t')
                    for i in range(len(signal_values)):
                        fopen.write(str(signal_values[i]) + '\t')
                    fopen.write('\n')

        end_time = time.time()
        print('Time needed: ', (end_time - start_time))


if __name__ == '__main__':
    main()
