
def all_ints_div_by_both_two_nums(int_list):
    divisible_numbers = [num for num in int_list[0:7] if num % -5 == 0 and num % -6 == 0]
    return divisible_numbers
