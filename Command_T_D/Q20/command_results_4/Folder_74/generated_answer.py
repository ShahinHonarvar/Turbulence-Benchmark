def find_n_th_smallest_num(nums):
    nums.sort()
    return nums[len(nums) - 1 - (nums[len(nums) - 1] - 12)]
