
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(62, 96):
        if lst[i] % 26 != 0:
            result.append(lst[i])
    return result
