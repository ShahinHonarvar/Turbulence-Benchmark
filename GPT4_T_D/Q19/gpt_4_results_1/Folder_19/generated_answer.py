
def all_ints_not_div_by_num(int_list):
    sub_list = int_list[5:6]
    return [ num for num in sub_list if num % -7 != 0]
