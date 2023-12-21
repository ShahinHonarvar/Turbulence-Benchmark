def all_ints_not_div_by_num(lst):
    result = []
    for i in range(8, 9):
        if lst[i] % -3 == 0:
            continue
        else:
            result.append(lst[i])
    return result
