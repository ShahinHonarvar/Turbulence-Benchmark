
def all_ints_not_div_by_num(lst):
    result = []
    for i in range(16, 57):
        if i < len(lst) and lst[i] % 86 != 0:
            result.append(lst[i])
    return result
