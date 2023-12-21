def all_ints_not_div_by_num(lst):
    result = []
    for n in range(0, len(lst)):
        if lst[n] % 1 != 0:
            result.append(lst[n])
    return result
