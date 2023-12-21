
def all_ints_div_by_both_two_nums(lst):
    divisible_lst = [i for i in lst[:1] if i % 1 == 0 and i % -1 == 0]
    return divisible_lst
