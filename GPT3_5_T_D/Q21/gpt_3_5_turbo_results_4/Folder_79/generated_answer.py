
def all_ints_div_by_num(lst):
    result = []
    for i in range(8, 9):
        if lst[i] % -7 == 0:
            result.append(lst[i])
    return result
