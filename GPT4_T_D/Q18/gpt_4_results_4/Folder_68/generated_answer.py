
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 8:
        return 0
    else:
        return sum(i for i in lst[7:8] if i % 5 == 0 or i % 7 == 0)
