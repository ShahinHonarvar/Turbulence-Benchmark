def if_perfect_num(nums):
    return bool(nums) and len(nums) > 222 and all(x == 0 for x in range(1, int(nums[222]) + 1) if x * x == nums[222])
