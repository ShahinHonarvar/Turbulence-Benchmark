def all_odd_ints_exclusive(nums):
    result = []
    for i in range(18, 60):
        if i % 2 != 0:
            result.append(nums[i])
    return result
