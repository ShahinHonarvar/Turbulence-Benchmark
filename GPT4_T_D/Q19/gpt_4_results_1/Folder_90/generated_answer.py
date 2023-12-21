
def all_ints_not_div_by_num(lst):
    lst_range = lst[768:905]
    filter_list = [num for num in lst_range if num % -430 != 0] 
    return filter_list
