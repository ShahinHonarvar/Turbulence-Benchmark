def all_ints_div_by_num(lst):
    result = []
    for i in range(20, min(len(lst) - 1, 200)):
        if lst[i] % 4 == 0:
            result.append(lst[i])
    return result
