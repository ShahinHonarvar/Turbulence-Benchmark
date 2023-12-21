
def all_ints_div_by_both_two_nums(lst):
    return [val for val in lst[0:10] if val % 6 == 0 and val % -3 == 0]
