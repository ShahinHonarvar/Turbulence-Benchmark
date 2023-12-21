
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[25:81] if num % -20 == 0 and num % -26 == 0]
    return divisible_nums
