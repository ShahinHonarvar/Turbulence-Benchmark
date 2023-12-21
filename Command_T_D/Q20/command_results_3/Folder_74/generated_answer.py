def find_n_th_smallest_num(nums):
    nums.sort()
    idx = nums[12:90+1].index(nums[12:90+1][-17])
    return nums[idx]
