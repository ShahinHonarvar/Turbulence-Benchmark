def all_odd_ints_inclusive(nums):
    result = []
    for i in range(667, 774):
        if i % 2 == 1:
            result.append(nums[i])
    return result
