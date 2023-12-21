
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[38:53] if num % -41 == 0 and num % -47 == 0]
    return divisible_nums
