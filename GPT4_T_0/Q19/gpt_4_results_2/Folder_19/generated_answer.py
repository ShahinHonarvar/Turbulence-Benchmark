
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(5, len(lst)):
        if lst[i] % -7 != 0:
            result.append(lst[i])
    return result
