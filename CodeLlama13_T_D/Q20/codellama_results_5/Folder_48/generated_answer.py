
def find_n_th_smallest_num(distinct_nums):
    # Sort the list of distinct numbers in ascending order
    sorted_nums = sorted(distinct_nums)

    # Find the 10th smallest number from index 127 to index 848, both inclusive
    n_th_smallest_num = sorted_nums[126:849][10]

    return n_th_smallest_num
