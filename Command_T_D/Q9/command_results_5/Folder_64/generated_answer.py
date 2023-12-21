def all_odd_ints_inclusive(nums):
    result = []
    for i in range(0, 5):
        if nums[i] % 2 == 1:
            result.append(nums[i])
    return result
