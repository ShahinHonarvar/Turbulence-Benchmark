
def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = [i for i in int_list[0:3] if i % -2 == 0 and i % 3 == 0]
    return divisible_by_both
