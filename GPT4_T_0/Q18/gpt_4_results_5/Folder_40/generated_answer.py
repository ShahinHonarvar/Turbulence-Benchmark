
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    else:
        return sum(i for i in lst[0:2] if i % 2 == 0 or i % 1 == 0)
