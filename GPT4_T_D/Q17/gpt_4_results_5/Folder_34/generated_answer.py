
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[60:201] if num % 9 == 0 and num % 11 == 0]
    return divisible_nums
