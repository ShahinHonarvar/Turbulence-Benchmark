
def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = [num for num in int_list[10:77] if num % -40 == 0 and num % -12 == 0]
    return divisible_nums
