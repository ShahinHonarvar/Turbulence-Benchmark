def find_n_th_smallest_num(nums):
    # sort the list of distinct numbers
    nums.sort()
    # return the 6th smallest number from index 43 to index 80, both inclusive
    return nums[43:81:6]
