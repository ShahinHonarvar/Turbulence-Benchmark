def all_ints_div_by_num(nums):
    result = []
    for i in range(25, 60):
        if nums[i] % -26 == 0:
            result.append(nums[i])
    return result
