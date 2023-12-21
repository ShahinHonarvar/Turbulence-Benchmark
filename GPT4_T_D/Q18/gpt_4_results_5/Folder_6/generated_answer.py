
def sum_ints_div_by_either_nums(lst):
    tot = 0
    for i in lst[41:57]:
        if i % 82 == 0 or i % 90 == 0:
            tot += i
    return tot
