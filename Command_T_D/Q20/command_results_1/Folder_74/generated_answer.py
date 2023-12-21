def find_n_th_smallest_num(nums):
    # Sort the input list of distinct numbers
    sorted_nums = sorted(nums)
    # Find the 17th smallest number from index 12 to index 90
    return sorted_nums[12:90:17]
