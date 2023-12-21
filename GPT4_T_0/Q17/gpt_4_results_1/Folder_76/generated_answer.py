
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[250:630] if num % 850 == 0 and num % 587 == 0]
    return divisible_nums
