def all_ints_not_div_by_num(lst):
    result = []
    for i in range(len(lst) - 22, -1, -1):
        if lst[i] % -46 != 0:
            result.append(lst[i])
    return result
