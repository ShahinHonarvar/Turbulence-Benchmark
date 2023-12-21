def all_odd_ints_exclusive(nums):
    return [i for i in range(len(nums) - 1) if nums[i] % 2 == 1]
