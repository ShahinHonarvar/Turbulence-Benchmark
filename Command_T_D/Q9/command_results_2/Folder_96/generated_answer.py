def all_odd_ints_inclusive(nums):
    return [i for i in range(50, len(nums) + 1, 2) if nums[i] % 2 == 1]
