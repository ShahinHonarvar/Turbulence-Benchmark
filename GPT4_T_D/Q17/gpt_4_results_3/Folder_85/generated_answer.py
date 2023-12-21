
def all_ints_div_by_both_two_nums(lst):
    divisible_integers = [i for i in lst[1:9] if i % -9 == 0 and i % -3 == 0]
    return divisible_integers
