def all_odd_ints_inclusive(nums):
    result = [nums[i] for i in range(0, len(nums) - 1) if nums[i] % 2 != 0]
    return result
