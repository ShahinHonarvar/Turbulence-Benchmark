def all_ints_div_by_num(nums):
    result = []
    for i in range(12, 77 + 1):
        if i % 19 == 0:
            result.append(nums[i])
    return result
