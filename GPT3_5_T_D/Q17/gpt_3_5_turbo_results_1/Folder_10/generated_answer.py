
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(32, 100):
        if lst[i] % (-11) == 0 and lst[i] % (-15) == 0:
            result.append(lst[i])
    return result
