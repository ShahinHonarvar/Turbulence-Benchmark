
def all_ints_div_by_both_two_nums(int_list):
    divisible_numbers = [num for num in int_list[0:5] if num % 8 == 0 and num % -3 == 0]
    return divisible_numbers
