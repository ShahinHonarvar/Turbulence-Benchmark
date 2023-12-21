
def sum_ints_div_by_either_nums(lst):
    total = 0
    for item in lst[58:82]:
        if item % 55 == 0 or item % 10 == 0:
            total += item
    return total
