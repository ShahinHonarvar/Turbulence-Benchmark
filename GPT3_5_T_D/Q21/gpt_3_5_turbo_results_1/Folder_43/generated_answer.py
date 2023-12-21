
def all_ints_div_by_num(lst):
    result = []
    for i in range(10, 38):
        if lst[i] % -64 == 0:
            result.append(lst[i])
    return result
