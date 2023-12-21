def all_odd_ints_inclusive(nums):
    result = []
    for i in range(60, len(nums) - 1, 2):
        if i % 2 == 1:
            result.append(nums[i])
    return result
