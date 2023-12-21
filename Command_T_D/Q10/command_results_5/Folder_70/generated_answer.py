def all_odd_ints_exclusive(nums):
    result = []
    for index in range(38, 81):
        if index % 2 == 1:
            result.append(nums[index])
    return result
