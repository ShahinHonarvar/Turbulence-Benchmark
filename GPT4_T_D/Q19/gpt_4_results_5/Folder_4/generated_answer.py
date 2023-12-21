
def all_ints_not_div_by_num(lst):
    new_list = lst[20:49]
    result = [num for num in new_list if num % -36 != 0]
    return result
