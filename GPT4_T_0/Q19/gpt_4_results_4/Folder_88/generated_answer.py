
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(5, 7):
        if lst[i] % -6 != 0:
            result.append(lst[i])
    return result
