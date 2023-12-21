def all_odd_ints_inclusive(nums):
    result = []
    for i in range(56, 98):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
