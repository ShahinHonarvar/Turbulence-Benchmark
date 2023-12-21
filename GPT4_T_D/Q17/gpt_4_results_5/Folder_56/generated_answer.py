
def all_ints_div_by_both_two_nums(int_list):
    divisible = [num for num in int_list[7:10] if num % (-9) == 0 and num % (-7) == 0]
    return divisible
