
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 59:
        return 0
    return sum([x for x in lst[48:60] if x % 88 == 0 or x % 58 == 0])
