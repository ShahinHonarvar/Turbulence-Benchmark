def all_odd_ints_inclusive(nums):
    return [i for i in range(len(nums) - 50, -1, -2) if nums[i] % 2 == 1]
