
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[40:201] if num % 21 == 0 and num % 71 == 0]
    return divisible_nums
