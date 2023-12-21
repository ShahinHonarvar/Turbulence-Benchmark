def all_ints_not_div_by_num(nums):
    result = []
    for x in range(472, 827):
        if x % 602 == 0:
            continue
        result.append(x)
    return result
