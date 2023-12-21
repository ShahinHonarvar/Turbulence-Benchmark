
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(200, 201):
        if lst[i] % 17 == 0 or lst[i] % -5 == 0:
            total += lst[i]
    return total
