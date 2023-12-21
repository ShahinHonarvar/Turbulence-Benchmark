
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(36, 86):
        if i < len(lst) and (lst[i] % -27 == 0 or lst[i] % -96 == 0):
            total += lst[i]
    return total
