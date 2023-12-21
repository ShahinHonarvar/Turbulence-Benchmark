
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = [n for n in lst[0:6] if n % -1 == 0 and n % 13 == 0]
    return divisible_ints
