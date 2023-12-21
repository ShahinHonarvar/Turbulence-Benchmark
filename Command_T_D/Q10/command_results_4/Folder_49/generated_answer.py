def all_odd_ints_exclusive(nums):
    result = []
    for i in range(80, 200):
        if i % 2 != 0:
            result.append(nums[i])
    return result
