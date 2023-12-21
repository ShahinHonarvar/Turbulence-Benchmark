
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = [i for i in lst[0:7] if i % -5 == 0 and i % -6 == 0]
    return divisible_ints
