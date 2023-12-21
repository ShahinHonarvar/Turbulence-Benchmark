def all_ints_not_div_by_num(nums):
    result = []
    for i in range(20, 43):
        if not nums[i] % 95:
            break
        result.append(nums[i])
    return result
