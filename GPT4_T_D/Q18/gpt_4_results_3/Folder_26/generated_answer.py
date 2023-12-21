
def sum_ints_div_by_either_nums(lst):
    sum = 0
    if len(lst) >= 71:
        for i in range(69, 71):
            if lst[i] % 72 == 0 or lst[i] % 70 == 0:
                sum += lst[i]
    return sum
