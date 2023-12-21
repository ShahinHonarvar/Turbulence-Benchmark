
def all_ints_div_by_both_two_nums(lst):
    lst = list(range(70, 200 + 1))
    return [x for x in lst if x % 3 == 0 and x % -300 == 0]
