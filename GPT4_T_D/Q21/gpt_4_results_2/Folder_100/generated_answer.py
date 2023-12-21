
def all_ints_div_by_num(lst):
    result = []
    for i in range(86, 93):
        if lst[i] % 86 == 0:
            result.append(lst[i])
    return result
