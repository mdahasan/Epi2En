"""
This code generates negative samples (non-enhancers) from the
enhancer file. The non-enhancers maintains similar min/max and mean
for their sample
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
sns.set(style="darkgrid")


def plot_hist(lengths, name):
    # plt.hist(enhancer_lengths, bins = 'auto')
    sns.distplot(lengths, norm_hist = False, kde = False)
    # plt.xlim(0, 10000)
    plt.xlabel('Nonenhancer region length')
    plt.ylabel('Count')
    plt.title(name)
    plt.show()


def main():
    strong_enhancer_file = sys.argv[1]
    all_enhancer_file = sys.argv[2]             # from DENdb
    cell_line_name = sys.argv[3]

    strong_enhancer_lengths = list()
    with open(strong_enhancer_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            enhancer_start_pos = int(cols[1])
            enhancer_end_pos = int(cols[2])

            strong_enhancer_lengths.append(enhancer_end_pos - enhancer_start_pos)

    plot_hist(strong_enhancer_lengths, cell_line_name)
    print np.min(strong_enhancer_lengths), np.max(strong_enhancer_lengths), np.mean(strong_enhancer_lengths), np.std(strong_enhancer_lengths)
    print len(strong_enhancer_lengths)





    # building negative samples (non-enhancers)
    # chr1_enhancer_positions_list = list()
    # chr2_enhancer_positions_list = list()
    # chr3_enhancer_positions_list = list()
    # chr4_enhancer_positions_list = list()
    # chr5_enhancer_positions_list = list()
    # chr6_enhancer_positions_list = list()
    # chr7_enhancer_positions_list = list()
    # chr8_enhancer_positions_list = list()
    # chr9_enhancer_positions_list = list()
    # chr10_enhancer_positions_list = list()
    # chr11_enhancer_positions_list = list()
    # chr12_enhancer_positions_list = list()
    # chr13_enhancer_positions_list = list()
    # chr14_enhancer_positions_list = list()
    # chr15_enhancer_positions_list = list()
    # chr16_enhancer_positions_list = list()
    # chr17_enhancer_positions_list = list()
    # chr18_enhancer_positions_list = list()
    # chr19_enhancer_positions_list = list()
    # chr20_enhancer_positions_list = list()
    # chr21_enhancer_positions_list = list()
    # chr22_enhancer_positions_list = list()
    # chrX_enhancer_positions_list = list()
    # chrY_enhancer_positions_list = list()
    #
    # with open(all_enhancer_file, 'r') as af:
    #     for line in af.readlines():
    #         line = line.strip()
    #         cols = line.split()
    #
    #         enhancer_start_pos = int(cols[1])
    #         enhancer_end_pos = int(cols[2])
    #
    #         if cols[0] == 'chr1':
    #             chr1_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr2':
    #             chr2_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr3':
    #             chr3_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr4':
    #             chr4_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr5':
    #             chr5_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr6':
    #             chr6_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr7':
    #             chr7_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr8':
    #             chr8_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr9':
    #             chr9_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr10':
    #             chr10_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         ##
    #
    #         if cols[0] == 'chr11':
    #             chr11_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr12':
    #             chr12_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr13':
    #             chr13_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr14':
    #             chr14_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr15':
    #             chr15_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr16':
    #             chr16_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr17':
    #             chr17_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr18':
    #             chr18_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr19':
    #             chr19_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr20':
    #             chr20_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr21':
    #             chr21_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chr22':
    #             chr22_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chrX':
    #             chrX_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    #         if cols[0] == 'chrY':
    #             chrY_enhancer_positions_list.append((enhancer_start_pos, enhancer_end_pos))
    #
    # chr1_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr2_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr3_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr4_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr5_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr6_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr7_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr8_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr9_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr10_enhancer_positions_list.sort(key=lambda tup: tup[1])
    #
    # chr11_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr12_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr13_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr14_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr15_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr16_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr17_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr18_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr19_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr20_enhancer_positions_list.sort(key=lambda tup: tup[1])
    #
    # chr21_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chr22_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chrX_enhancer_positions_list.sort(key=lambda tup: tup[1])
    # chrY_enhancer_positions_list.sort(key=lambda tup: tup[1])
    #
    # # building negative enahcners with similar sizes of enhancers from enhancer list
    # f_non_enhancer = open(str(cell_line_name) + '_nonenhancers.txt', 'w')
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr1_enhancer_positions_list)):
    #     previous_enh_end_pos = chr1_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr1_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr1' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr2_enhancer_positions_list)):
    #     previous_enh_end_pos = chr2_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr2_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr2' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr3_enhancer_positions_list)):
    #     previous_enh_end_pos = chr3_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr3_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr3' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr4_enhancer_positions_list)):
    #     previous_enh_end_pos = chr4_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr4_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr4' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr5_enhancer_positions_list)):
    #     previous_enh_end_pos = chr5_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr5_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr5' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr6_enhancer_positions_list)):
    #     previous_enh_end_pos = chr6_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr6_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr6' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr7_enhancer_positions_list)):
    #     previous_enh_end_pos = chr7_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr7_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr7' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr8_enhancer_positions_list)):
    #     previous_enh_end_pos = chr8_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr8_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr8' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr9_enhancer_positions_list)):
    #     previous_enh_end_pos = chr9_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr9_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr9' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr10_enhancer_positions_list)):
    #     previous_enh_end_pos = chr10_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr10_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr10' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # ###
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr11_enhancer_positions_list)):
    #     previous_enh_end_pos = chr11_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr11_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr11' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr12_enhancer_positions_list)):
    #     previous_enh_end_pos = chr12_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr12_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr12' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr13_enhancer_positions_list)):
    #     previous_enh_end_pos = chr13_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr13_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr13' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr14_enhancer_positions_list)):
    #     previous_enh_end_pos = chr14_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr14_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr14' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr15_enhancer_positions_list)):
    #     previous_enh_end_pos = chr15_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr15_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr15' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr16_enhancer_positions_list)):
    #     previous_enh_end_pos = chr16_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr16_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr16' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr17_enhancer_positions_list)):
    #     previous_enh_end_pos = chr17_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr17_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr17' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr18_enhancer_positions_list)):
    #     previous_enh_end_pos = chr18_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr18_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr18' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr19_enhancer_positions_list)):
    #     previous_enh_end_pos = chr19_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr19_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr19' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr20_enhancer_positions_list)):
    #     previous_enh_end_pos = chr20_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr20_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr20' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr21_enhancer_positions_list)):
    #     previous_enh_end_pos = chr21_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr21_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr21' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chr22_enhancer_positions_list)):
    #     previous_enh_end_pos = chr22_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chr22_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chr22' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chrX_enhancer_positions_list)):
    #     previous_enh_end_pos = chrX_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chrX_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chrX' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # strong_enhancer_lengths_index = 0
    # random.shuffle(strong_enhancer_lengths)
    # for i in range(1, len(chrY_enhancer_positions_list)):
    #     previous_enh_end_pos = chrY_enhancer_positions_list[i-1][1]
    #     current_enh_start_pos = chrY_enhancer_positions_list[i][0]
    #
    #     strong_enh_length = strong_enhancer_lengths[strong_enhancer_lengths_index]
    #
    #     if (current_enh_start_pos - previous_enh_end_pos) > strong_enh_length + 200:
    #         f_non_enhancer.write('chrY' + ' ' + str(previous_enh_end_pos + 100) + ' ' + str(previous_enh_end_pos + 100 + strong_enh_length) + '\n')
    #
    #     strong_enhancer_lengths_index += 1
    #
    #     if strong_enhancer_lengths_index == len(strong_enhancer_lengths):
    #         strong_enhancer_lengths_index = 0
    #
    # f_non_enhancer.close()


if __name__ == "__main__":
    main()
