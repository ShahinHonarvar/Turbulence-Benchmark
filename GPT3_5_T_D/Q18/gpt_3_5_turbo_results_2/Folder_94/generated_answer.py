
def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(93, 95):
        if lst[i] % (-53) == 0 or lst[i] % (-91) == 0:
            total += lst[i]
    return total
