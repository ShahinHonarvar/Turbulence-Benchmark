
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(29, 54):
        if lst[i] % -68 == 0 and lst[i] % -85 == 0:
            result.append(lst[i])
    return result
