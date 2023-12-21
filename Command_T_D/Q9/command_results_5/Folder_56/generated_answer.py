def all_odd_ints_inclusive(nums):
    result = [i for i in range(0, len(nums)) if nums[i] % 2 == 1]
    return result
