
def all_ints_not_div_by_num(lst):
    sublist = lst[91:200]
    result = [num for num in sublist if num % -31 != 0]
    return result
