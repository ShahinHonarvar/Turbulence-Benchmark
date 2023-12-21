
def sum_ints_div_by_either_nums(lst):
    sum_ints = 0
    for i in range(73, 87):
        if i < len(lst) and (lst[i] % 54 == 0 or lst[i] % 82 == 0):
            sum_ints += lst[i]
    return sum_ints
