
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(828, 933):
        if lst[i] % -649 == 0 or lst[i] % -461 == 0:
            total += lst[i]
    return total
