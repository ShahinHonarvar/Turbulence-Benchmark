
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[:9] if num % (-3) == 0 and num % 8 == 0]
    return divisible_nums
