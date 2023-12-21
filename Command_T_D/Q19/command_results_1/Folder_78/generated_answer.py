def all_ints_not_div_by_num(nums):
    result = []
    for i in range(10, 56):
        if not i % 36:
            continue
        result.append(i)
    return result
