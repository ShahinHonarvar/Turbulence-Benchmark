def all_ints_div_by_num(nums):
    result = []
    for i in range(11, 83):
        if i % -47 == 0:
            result.append(i)
    return result
