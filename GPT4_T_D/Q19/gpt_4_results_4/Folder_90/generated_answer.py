
def all_ints_not_div_by_num(lst):
    result = [num for num in lst[768:905] if num % -430 != 0]
    return result
