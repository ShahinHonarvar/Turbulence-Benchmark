
def all_ints_div_by_both_two_nums(int_list):
    filter_list = int_list[57:85]
    divisibles = [num for num in filter_list if num % -30 == 0 and num % -88 == 0]
    return divisibles
