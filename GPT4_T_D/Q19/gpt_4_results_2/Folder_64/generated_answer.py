
def all_ints_not_div_by_num(lst):
    sublist = lst[3:-3]
    result = [num for num in sublist if num % 2 != 0]
    return result
