
def all_ints_not_div_by_num(int_list):
    result = [num for num in int_list[51:81] if num % 64 != 0]
    return result
