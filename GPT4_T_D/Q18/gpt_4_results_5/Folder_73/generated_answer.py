
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(81, 87):
        if i < len(lst) and (lst[i] % -33 == 0 or lst[i] % -62 == 0):
            total += lst[i]
    return total
