
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(24, 32):
        if lst[i] % 35 != 0:
            result.append(lst[i])
    return result
