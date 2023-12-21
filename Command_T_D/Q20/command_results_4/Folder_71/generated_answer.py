def find_n_th_smallest_num(nums):
    nums.sort()
    return nums[len(nums) - nums[56:70].index(min(nums[56:70])) - 1]
