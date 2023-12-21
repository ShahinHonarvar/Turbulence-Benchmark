
def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list[:4] if num % 11 == 0 and num % -7 == 0]
