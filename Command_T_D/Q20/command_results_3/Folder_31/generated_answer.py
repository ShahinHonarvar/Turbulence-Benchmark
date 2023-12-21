def find_n_th_smallest_num(nums):
    # sort the list of distinct numbers
    sorted_nums = sorted(nums)
    # find the 9th smallest number from index 82 to index 93, both inclusive
    9th_smallest_num = sorted_nums[82]
    for i in range(82, 93):
        9th_smallest_num = min(9th_smallest_num, sorted_nums[i])
    return 9th_smallest_num
