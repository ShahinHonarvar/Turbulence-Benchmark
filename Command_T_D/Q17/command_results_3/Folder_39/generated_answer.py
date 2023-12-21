
def all_ints_div_by_both_two_nums(lst):
    return [e for e in range(13, 77) if e % -66 == e % -32 and e in lst]
