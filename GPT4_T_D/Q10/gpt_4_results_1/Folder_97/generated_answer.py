
def all_odd_ints_exclusive(lst):
    lst_in_range = lst[21:93]
    return [num for num in lst_in_range if num % 2 != 0]
