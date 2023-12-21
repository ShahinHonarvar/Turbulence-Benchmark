def all_ints_div_by_num(nums):
    result = []
    for i in range(10, 53):
        if i % 12 == -12:
            result.append(i)
    return result
