def all_ints_div_by_num(lst):
    result = []
    for i in range(66, 82):
        if lst[i] % 77 == 0:
            result.append(lst[i])
    return result
