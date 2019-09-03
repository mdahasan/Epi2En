"""
This code takes in the "enhancer.csv" file downloaded from
http://www.cbrc.kaust.edu.sa/dendb/index.php


The file contains list of enhancers of all cell lines involved
in the experiment. This code seperates the enahncers into
cell line specific enhancer files
"""

import sys


def main():
    complete_enhancer_file = sys.argv[1]

    f_Gm12878 = open('Gm12878_enhancers.txt', 'w')
    f_H1hesc = open('H1hesc_enhancers.txt', 'w')
    f_Huvec = open('Huvec_enhancers.txt', 'w')
    f_Helas3 = open('Helas3_enhancers.txt', 'w')
    f_Hepg2 = open('Hepg2_enhancers.txt', 'w')
    f_K562 = open('K562_enhancers.txt', 'w')

    with open(complete_enhancer_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split(',')

            cell_line = cols[4]
            chromosome = cols[1]
            enhance_start = cols[2]
            enhancer_end = cols[3]

            if cell_line == 'Gm12878':
                f_Gm12878.write(str(chromosome) + ' ' + str(enhance_start) + ' ' + str(enhancer_end) + '\n')

            if cell_line == 'H1hesc':
                f_H1hesc.write(str(chromosome) + ' ' + str(enhance_start) + ' ' + str(enhancer_end) + '\n')

            if cell_line == 'Huvec':
                f_Huvec.write(str(chromosome) + ' ' + str(enhance_start) + ' ' + str(enhancer_end) + '\n')

            if cell_line == 'Helas3':
                f_Helas3.write(str(chromosome) + ' ' + str(enhance_start) + ' ' + str(enhancer_end) + '\n')

            if cell_line == 'Hepg2':
                f_Hepg2.write(str(chromosome) + ' ' + str(enhance_start) + ' ' + str(enhancer_end) + '\n')

            if cell_line == 'K562':
                f_K562.write(str(chromosome) + ' ' + str(enhance_start) + ' ' + str(enhancer_end) + '\n')

    f_Gm12878.close()
    f_H1hesc.close()
    f_Huvec.close()
    f_Helas3.close()
    f_Hepg2.close()
    f_K562.close()


if __name__ == '__main__':
    main()
