def all_odd_ints_exclusive(nums):
    result = []
    for i in range(70, 98):
        if i % 2 != 0:
            result.append(nums[i])
    return result
