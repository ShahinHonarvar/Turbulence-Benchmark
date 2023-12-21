def all_odd_ints_inclusive(nums):
    return [i for i in range(0, len(nums)) if nums[i] % 2 == 1]
