def all_odd_ints_exclusive(nums):
    odds = [i for i in range(2, len(nums)-1) if nums[i] % 2 == 1]
    return [nums[i] for i in odds]
