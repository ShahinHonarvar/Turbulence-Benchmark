
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 95:
        return 0
    return sum([i for i in lst[93:95] if i % -53 == 0 or i % -91 == 0])
