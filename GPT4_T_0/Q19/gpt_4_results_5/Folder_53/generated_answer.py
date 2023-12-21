
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(200, 202):
        if lst[i] % -200 != 0:
            result.append(lst[i])
    return result
