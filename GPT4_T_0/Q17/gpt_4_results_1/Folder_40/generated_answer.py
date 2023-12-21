
def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 2:
        return []
    else:
        return [i for i in lst[0:2] if i % 2 == 0 and i % 1 == 0]
