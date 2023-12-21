
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(25, 45):
        if i < len(lst) and lst[i] % -72 != 0:
            result.append(lst[i])
    return result
