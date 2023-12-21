
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(19, 37):
        if lst[i] % -67 != 0:
            result.append(lst[i])
    return result
