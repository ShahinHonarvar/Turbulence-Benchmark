
def all_ints_not_div_by_num(lst):
    sublist = lst[8:9]
    result = [num for num in sublist if num % -9 != 0]
    return result
