
def all_ints_div_by_both_two_nums(int_list):
    result_list = [num for num in int_list[61:89] if num % 31 == 0 and num % 11 == 0]
    return result_list
