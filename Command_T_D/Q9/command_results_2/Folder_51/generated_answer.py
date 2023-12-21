def all_odd_ints_inclusive(nums):
    result = []
    for i in range(1, len(nums)+1):
        if nums[i-1] % 2 == 0:
            break
        result.append(nums[i-1])
    return result
