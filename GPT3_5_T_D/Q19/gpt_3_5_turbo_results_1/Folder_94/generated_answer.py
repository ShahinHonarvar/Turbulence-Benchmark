
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(24, 45):
        if i % -72 != 0:
            result.append(lst[i])
    return result
