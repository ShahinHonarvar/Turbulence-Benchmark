
def all_ints_not_div_by_num(lst):
    new_list = lst[3:-1]
    result = [num for num in new_list if num % 2 != 0]
    return result
