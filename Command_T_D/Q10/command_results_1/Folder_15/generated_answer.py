def all_odd_ints_exclusive(nums):
    return [nums[i] for i in range(0, len(nums)-1) if nums[i] % 2 == 1]
