
def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = [x for x in int_list[0:7] if x % -5 == 0 and x % -6 == 0]
    return divisible_ints
