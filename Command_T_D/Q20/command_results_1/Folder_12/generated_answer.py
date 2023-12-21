def find_n_th_smallest_num(nums):
    nums.sort()
    idx = nums.index(min(nums[40:68]))
    return nums[idx + 13]
