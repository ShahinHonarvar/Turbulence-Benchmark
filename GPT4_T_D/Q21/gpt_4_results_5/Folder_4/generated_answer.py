
def all_ints_div_by_num(lst):
    result = []
    for i in range(12, 93):
        if i < len(lst) and lst[i] % -14 == 0:
            result.append(lst[i])
    return result
