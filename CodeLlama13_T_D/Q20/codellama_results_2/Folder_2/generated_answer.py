
def find_n_th_smallest_num(distinct_numbers):
    # sort the list of distinct numbers
    sorted_distinct_numbers = sorted(distinct_numbers)
    # return the 8th smallest number from index 23 to index 65, both inclusive
    return sorted_distinct_numbers[23:66][7]
