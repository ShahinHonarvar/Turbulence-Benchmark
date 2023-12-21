
def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(25, 81):
        if lst[i] % -20 == 0 and lst[i] % -26 == 0:
            result.append(lst[i])
    return result
