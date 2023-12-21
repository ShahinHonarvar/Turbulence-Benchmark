
def all_ints_div_by_both_two_nums(num_list):
    divisible_nums = [i for i in num_list[0:5] if i % 8 == 0 and i % -3 == 0]
    return divisible_nums
