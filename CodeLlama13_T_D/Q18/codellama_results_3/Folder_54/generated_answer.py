
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(13, 92):
        if lst[i] % -65 == 0 or lst[i] % -62 == 0:
            total += lst[i]
    return total
