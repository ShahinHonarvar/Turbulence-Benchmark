
def all_ints_div_by_num(lst):
    result = []
    for i in range(12, 93):
        if lst[i] % -14 == 0:
            result.append(lst[i])
    return result
