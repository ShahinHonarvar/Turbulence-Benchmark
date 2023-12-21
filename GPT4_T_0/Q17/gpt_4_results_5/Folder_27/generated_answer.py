
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(20, 36):
        if lst[i] % -36 == 0 and lst[i] % -89 == 0:
            result.append(lst[i])
    return result
