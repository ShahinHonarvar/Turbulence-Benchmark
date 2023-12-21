
def all_ints_div_by_both_two_nums(lst):
    return [x for x in lst[1:-1] if x % -9 == x % -3 == 0]
