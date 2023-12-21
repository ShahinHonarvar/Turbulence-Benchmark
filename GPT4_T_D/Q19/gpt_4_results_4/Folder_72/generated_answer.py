
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(14, min(70, len(lst))):
        if lst[i] % -78 != 0:
            result.append(lst[i])
    return result
