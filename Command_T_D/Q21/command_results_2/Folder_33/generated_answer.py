def all_ints_div_by_num(nums):
    result = []
    for i in range(319, 612):
        if nums[i] % -215 == 0:
            result.append(i)
    return result
