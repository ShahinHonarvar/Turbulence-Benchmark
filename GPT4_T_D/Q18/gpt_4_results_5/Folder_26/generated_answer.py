
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(69, 71):
        if i < len(lst):
            if lst[i] % 72 == 0 or lst[i] % 70 == 0:
                total += lst[i]
    return total
