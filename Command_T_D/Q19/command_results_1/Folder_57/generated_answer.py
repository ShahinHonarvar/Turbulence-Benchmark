import bisect
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(56, 88):
        if lst[i] % -59 != 0:
            result.append(lst[i])
    return result
