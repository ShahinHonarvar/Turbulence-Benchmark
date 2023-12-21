
def all_ints_div_by_both_two_nums(ints):
    if len(ints) < 2:
        return []
    else:
        return [i for i in ints[:2] if i % -6 == 0 and i % 4 == 0]
