def find_n_th_smallest_num(nums):
    return sorted(nums)[len(nums) - 2 - nums[2] if nums[0] == nums[1] else len(nums) - 2 - nums[2] - 1]
