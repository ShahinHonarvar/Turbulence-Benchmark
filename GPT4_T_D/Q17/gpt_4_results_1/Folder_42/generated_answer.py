
def all_ints_div_by_both_two_nums(lst):
    result = [val for val in lst[29:46] if val % 27 == 0 and val % 81 == 0]
    return result
