
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[72:94] if num % 32 == 0 and num % 44 == 0]
    return divisible_nums
