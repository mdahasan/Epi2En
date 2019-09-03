"""
1. This code takes the enhancer/non-enhancer file and
rewrite the enhancer/non-enhancer samples of equal size.
Since the lenght of enhancer/non-enhancer are not equal, this
code makes all the sample of size 200bp
"""

import sys


def main():
    sample_file = sys.argv[1]       # enhancer/non-enhancer original bed file
    file_name = sys.argv[2]         # cell_line_class_type name

    fopen = open(str(file_name) + '.txt', 'w')

    with open(sample_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            chromosome = cols[0]
            start_pos = int(cols[1])
            end_pos = int(cols[2])

            if (end_pos - start_pos) >= 200:
                start = start_pos
                end = start_pos + 200
                while end <= end_pos:
                    fopen.write(str(chromosome) + '\t' + str(start) + '\t' + str(end) + '\n')
                    start = end
                    end = end + 200


if __name__ == '__main__':
    main()
