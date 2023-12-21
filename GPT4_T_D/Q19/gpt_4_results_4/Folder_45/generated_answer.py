
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(31, min(200, len(lst))):
        if lst[i] % -115 != 0:
            result.append(lst[i])
    return result
