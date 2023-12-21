def find_n_th_smallest_num(nums):
    idx = nums.index(min(nums[145:156])) + 145
    return nums[idx]
