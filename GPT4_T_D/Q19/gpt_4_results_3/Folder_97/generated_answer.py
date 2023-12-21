
def all_ints_not_div_by_num(int_list):
    sub_list = int_list[15:48]
    not_div_by_16 = [num for num in sub_list if num % 16 != 0]
    return not_div_by_16
