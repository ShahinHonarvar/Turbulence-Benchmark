
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(21, 35):
        if lst[i] % -36 != 0:
            result.append(lst[i])
    return result
