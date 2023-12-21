def find_n_th_smallest_num(nums):
    # sort nums in reverse order
    sorted_nums = sorted(nums, reverse=True)
    # find the index of the n-th element
    index = sorted_nums[24:37].index(nums[24:37][13])
    # return the element at that index
    return sorted_nums[index]
