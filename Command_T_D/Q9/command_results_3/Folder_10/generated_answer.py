def all_odd_ints_inclusive(nums):
    result = []
    for i in range(25, 59):
        if i % 2 == 1:
            result.append(nums[i])
    return result
