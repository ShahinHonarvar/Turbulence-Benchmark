
def all_ints_div_by_num(lst):
    result = []
    if len(lst) > 0:
        if lst[0] % 7 == 0:
            result.append(lst[0])
    return result
