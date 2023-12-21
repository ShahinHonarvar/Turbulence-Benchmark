
def all_ints_div_by_both_two_nums(lst):
    lst = list(range(35, 65))
    return [i for i in lst if i % -30 == i % -95]
