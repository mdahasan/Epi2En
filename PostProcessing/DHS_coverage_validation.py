"""
This code takes the DHS bed file for each cell line and the prdicted
enhancer region bed file. It computes the overlap in bp for the predicted
enhancer that overlaps with DHS
"""

import sys


def main():
    DHS_bed_file = sys.argv[1]
    enhancer_bed_file = sys.argv[2]

    DHS_list = list()
    total_DHS_bp = 0
    with open(DHS_bed_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            chromosome = cols[0]
            start = int(cols[1])
            end = int(cols[2])

            total_DHS_bp += (end - start)

            DHS_list.append([chromosome, start, end])

    enhancer_covering_DHS_bp = 0
    complete_overlap = 0
    left_overlap = 0
    right_overlap = 0
    total_overlap = 0
    with open(enhancer_bed_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            chromosome = cols[0]
            start = int(cols[1])
            end = int(cols[2])

            for i in range(len(DHS_list)):
                if chromosome == DHS_list[i][0]:
                    if DHS_list[i][1] <= start <= end <= DHS_list[i][2]:
                        enhancer_covering_DHS_bp += (end - start)
                        complete_overlap +=1
                    if DHS_list[i][1] < start <= DHS_list[i][2] < end:
                        enhancer_covering_DHS_bp += (DHS_list[i][2] - start)
                        left_overlap += 1
                    if start < DHS_list[i][1] <= end < DHS_list[i][2]:
                        enhancer_covering_DHS_bp += (end - DHS_list[i][1])
                        right_overlap += 1

    total_overlap = complete_overlap + left_overlap + right_overlap

    print "Complete overlap: ", complete_overlap
    print "Left overlap: ", left_overlap
    print "Right overlap: ", right_overlap
    print "Overlap Precentage (%): ", (float(total_overlap)/float(len(DHS_list))) * 100
    print "Total DHS bp: ", total_DHS_bp
    print "Enhancer covered DHS bp: ", enhancer_covering_DHS_bp
    print "Percentage (%): ", (float(enhancer_covering_DHS_bp)/float(total_DHS_bp)) * 100



if __name__ == '__main__':
    main()
