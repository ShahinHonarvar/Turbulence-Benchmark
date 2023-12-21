
def all_ints_not_div_by_num(lst):
    temp_list = lst[23:97]
    result_list = [num for num in temp_list if num % -46 != 0]
    return result_list
