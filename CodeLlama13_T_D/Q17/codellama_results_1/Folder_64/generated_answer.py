
def all_ints_div_by_both_two_nums(lst):
    return [i for i in lst if i % 11 == 0 and i % -7 == 0][:4]
