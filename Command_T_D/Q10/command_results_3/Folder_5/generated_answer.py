def all_odd_ints_exclusive(nums):
    return [i for i in range(2, len(nums) - 1) if nums[i] % 2 == 1]
