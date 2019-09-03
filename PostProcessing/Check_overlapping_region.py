"""
This code takes two bed files and checks the number of bases are
overlapped between ranges in two file
"""

import sys

def main():
    bed_file1 = sys.argv[1]     # large non-enhancer file
    bed_file2 = sys.argv[2]     # enhancer file
    cell_line_name = sys.argv[3]

    bed_file1_entry_list = list()
    with open(bed_file1, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            bed_file1_entry_list.append([cols[0], int(cols[1]), int(cols[2])])

    complete_intersection_count = 0
    left_intersection_count = 0
    right_intersection_count = 0

    to_remove_from_bed_1 = list()

    with open(bed_file2, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            cols = line.split()

            chromosome = cols[0]
            start = int(cols[1])
            end = int(cols[2])

            for i in range(len(bed_file1_entry_list)):
                # complete interaction
                if chromosome == bed_file1_entry_list[i][0]:
                    if bed_file1_entry_list[i][1] <= start <= end <= bed_file1_entry_list[i][2]:
                        to_remove_from_bed_1.append([bed_file1_entry_list[i][0], bed_file1_entry_list[i][1], bed_file1_entry_list[i][2]])
                        complete_intersection_count += 1
                    elif bed_file1_entry_list[i][1] < start <= bed_file1_entry_list[i][2] < end:
                        to_remove_from_bed_1.append([bed_file1_entry_list[i][0], bed_file1_entry_list[i][1], bed_file1_entry_list[i][2]])
                        left_intersection_count += 1
                    elif start < bed_file1_entry_list[i][1] <= bed_file1_entry_list[i][2] < end:
                        to_remove_from_bed_1.append([bed_file1_entry_list[i][0], bed_file1_entry_list[i][1], bed_file1_entry_list[i][2]])
                        right_intersection_count += 1

    print "Complete intersection: ", complete_intersection_count
    print "Left intersection: ", left_intersection_count
    print "Right intersection: ", right_intersection_count
    print "Total non-ehnacer file size: ", len(bed_file1_entry_list)

    # removing intersecting samples
    # new_bed_file1_entry_list = list()
    # for i in range(len(bed_file1_entry_list)):
    #     chromosome = bed_file1_entry_list[i][0]
    #     start = bed_file1_entry_list[i][1]
    #     end = bed_file1_entry_list[i][2]
    #
    #     to_keep = True
    #     for j in range(len(to_remove_from_bed_1)):
    #         if chromosome == to_remove_from_bed_1[j][0] and start == to_remove_from_bed_1[j][1] and end == to_remove_from_bed_1[j][2]:
    #             to_keep = False
    #             break
    #
    #     if to_keep:
    #         new_bed_file1_entry_list.append([chromosome, start, end])
    #
    #
    # fopen = open(str(cell_line_name) + '_non_enhancers.txt', 'w')
    # for i in range(len(new_bed_file1_entry_list)):
    #     fopen.write(str(new_bed_file1_entry_list[i][0]) + ' ' + str(new_bed_file1_entry_list[i][1]) + ' ' + str(new_bed_file1_entry_list[i][2]) + '\n')
    #
    # fopen.close()

    ####################3 This part is to check if any overlap exists again #########################
    # print "After removing overlapping samples from non-enhancer..."
    # print "New non-enhancer file size: ", len(new_bed_file1_entry_list)
    # complete_intersection_count = 0
    # left_intersection_count = 0
    # right_intersection_count = 0
    #
    # # check again
    # with open(bed_file2, 'r') as f:
    #     for line in f.readlines():
    #         line = line.strip()
    #         cols = line.split()
    #
    #         chromosome = cols[0]
    #         start = int(cols[1])
    #         end = int(cols[2])
    #
    #         for i in range(len(new_bed_file1_entry_list)):
    #             # complete interaction
    #             if chromosome == new_bed_file1_entry_list[i][0]:
    #                 if new_bed_file1_entry_list[i][1] <= start <= end <= new_bed_file1_entry_list[i][2]:
    #                     complete_intersection_count += 1
    #                 elif new_bed_file1_entry_list[i][1] < start <= new_bed_file1_entry_list[i][2] < end:
    #                     left_intersection_count += 1
    #                 elif start < new_bed_file1_entry_list[i][1] <= new_bed_file1_entry_list[i][2] < end:
    #                     right_intersection_count += 1
    #
    # print "Complete intersection: ", complete_intersection_count
    # print "Left intersection: ", left_intersection_count
    # print "Right intersection: ", right_intersection_count
    #




if __name__ == '__main__':
    main()
