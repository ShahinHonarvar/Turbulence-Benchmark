
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[70:201] if num % 3 == 0 and num % -300 == 0]
    return divisible_nums
