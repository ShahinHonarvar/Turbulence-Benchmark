
def all_ints_div_by_both_two_nums(lst):
    return [x for x in lst[200:-200:-1] if x % 17 == x % -5 == 0]
