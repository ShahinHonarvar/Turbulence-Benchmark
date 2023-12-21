def find_n_th_smallest_num(nums):
    # sort by value
    nums.sort()
    # find the range index
    start = nums.index(nums[75])
    end = nums.index(nums[91])
    # find the 11th number
    return nums[start + 10]
