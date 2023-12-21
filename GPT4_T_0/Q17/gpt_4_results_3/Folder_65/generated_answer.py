
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[50:93] if num % -94 == 0 and num % -95 == 0]
    return divisible_nums
