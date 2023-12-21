def all_odd_ints_exclusive(nums):
    result = []
    for i in range(0, 2):
        if nums[i] % 2 == 0:
            break
        result.append(nums[i])
    return result
