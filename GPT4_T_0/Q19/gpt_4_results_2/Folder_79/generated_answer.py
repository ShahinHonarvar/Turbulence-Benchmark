
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(9, len(lst)):
        if lst[i] % -3 != 0:
            result.append(lst[i])
    return result
