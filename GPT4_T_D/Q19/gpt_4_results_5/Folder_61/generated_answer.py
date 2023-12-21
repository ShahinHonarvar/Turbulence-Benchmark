
def all_ints_not_div_by_num(lst):
    result = [num for num in lst[1:6] if num % -6 != 0]
    return result
