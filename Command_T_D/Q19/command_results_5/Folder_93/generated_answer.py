def all_ints_not_div_by_num(lst):
    result = []
    for i in range(33, 78):
        if lst[i] % -17 != 0:
            result.append(lst[i])
    return result
