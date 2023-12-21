
def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = [num for num in int_list[:10] if num % 10 == 0 and num % 100 == 0]
    return divisible_ints
