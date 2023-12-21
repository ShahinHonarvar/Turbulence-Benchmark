def find_n_th_smallest_num(nums):
    # sort the list
    nums.sort()
    # get the index of the nth element
    index = nums[8]
    # return the element at the index
    return nums[index - 1]
