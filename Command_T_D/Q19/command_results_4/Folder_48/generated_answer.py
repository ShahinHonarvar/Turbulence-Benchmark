def all_ints_not_div_by_num(nums):
    result = []
    for i in range(767, 938):
        if i % 593 != 0:
            result.append(i)
    return result
