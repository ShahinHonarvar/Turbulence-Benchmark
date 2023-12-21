
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(495, 826):
        if lst[i] % -201 != 0:
            result.append(lst[i])
    return result
