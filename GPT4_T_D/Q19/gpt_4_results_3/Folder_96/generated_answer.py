
def all_ints_not_div_by_num(int_list):
    new_list = int_list[51:200]
    result = [num for num in new_list if num % -34 != 0]
    return result
