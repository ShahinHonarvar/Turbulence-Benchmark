
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(22, 25):
        if lst[i] % -85 == 0 and lst[i] % -30 == 0:
            result.append(lst[i])
    return result
