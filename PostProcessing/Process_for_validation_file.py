"""
This code process the *_for_validation file to build in
a bed file
"""

import sys

def main():
    for_validation_file = sys.argv[1]

    name = for_validation_file.split('_')[0] + '_' + for_validation_file.split('_')[1]

    fopen = open(str(name) + '_predicetd_enhancers_regions.txt', 'w')

    check_dict = dict()

    with open(for_validation_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()
            loc_info = cols[0]
            predicted_class = int(cols[1])

            if loc_info not in check_dict and predicted_class == 1:
                check_dict[loc_info] = True
                chromosome = loc_info.split('_')[0]
                start = loc_info.split('_')[1]
                end = loc_info.split('_')[2]

                fopen.write(str(chromosome) + '\t' + str(start) + '\t' + str(end) + '\n')
    fopen.close()


if __name__ == '__main__':
    main()
