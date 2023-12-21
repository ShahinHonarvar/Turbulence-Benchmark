
def all_ints_div_by_num(lst):
    result = []
    for i in range(59, 78):
        if lst[i] % -95 == 0:
            result.append(lst[i])
    return result
