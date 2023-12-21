
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [i for i in int_list[28:97] if i % 90 == 0 and i % 97 == 0]
    return divisible_nums
