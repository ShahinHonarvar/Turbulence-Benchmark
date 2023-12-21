
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(30, 53):
        if lst[i] % -68 != 0:
            result.append(lst[i])
    return result
