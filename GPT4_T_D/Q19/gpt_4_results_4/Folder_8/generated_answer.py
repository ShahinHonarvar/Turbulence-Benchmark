
def all_ints_not_div_by_num(int_list):
    sub_list = int_list[18:88]
    result = [num for num in sub_list if num % -75 != 0]
    return result
