def all_ints_div_by_num(nums):
    result = []
    for i in range(11, 111):
        if i % 11 == 0:
            result.append(i)
    return result
