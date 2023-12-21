def all_odd_ints_exclusive(nums):
    return [nums[i] for i in range(len(nums)) if nums[i] % 2 == 1 and i != 3]
