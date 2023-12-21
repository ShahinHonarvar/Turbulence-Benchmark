
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(64, 80):
        if lst[i] % -95 != 0:
            result.append(lst[i])
    return result
