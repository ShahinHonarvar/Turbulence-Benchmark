
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(25, len(lst)):
        if lst[i] % -30 != 0:
            result.append(lst[i])
    return result
