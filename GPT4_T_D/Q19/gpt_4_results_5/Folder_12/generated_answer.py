
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(60, 93):
        if lst[i] % -26 != 0:
            result.append(lst[i])
    return result
