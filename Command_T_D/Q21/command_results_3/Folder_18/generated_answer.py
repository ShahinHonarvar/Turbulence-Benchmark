def all_ints_div_by_num(lst):
    result = []
    for i in range(26, 75):
        if lst[i] % 80 == 0:
            result.append(lst[i])
    return result
