
def all_ints_not_div_by_num(int_list):
    result = [num for num in int_list[768:905] if num % -430 != 0]
    return result
