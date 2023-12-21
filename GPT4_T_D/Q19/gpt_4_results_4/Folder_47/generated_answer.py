
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(26, min(76, len(lst))):
        if lst[i] % -53 != 0:
            result.append(lst[i])
    return result
