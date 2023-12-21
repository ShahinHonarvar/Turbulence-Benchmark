def all_ints_div_by_num(nums):
    result = []
    for i in range(42, 89+1):
        if nums[i] % -59 == 0:
            result.append(nums[i])
    return result
