
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(104, 574):
        if lst[i] % -514 != 0:
            result.append(lst[i])
    return result
