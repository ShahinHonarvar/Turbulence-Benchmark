def find_n_th_smallest_num(nums):
    # sort
    sorted_nums = sorted(nums)
    # num_index = nth index in the sorted array
    num_index = sorted_nums[20:200:11]
    # return the number at the index
    return nums[num_index - 1]
