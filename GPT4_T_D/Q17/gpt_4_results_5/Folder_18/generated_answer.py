
def all_ints_div_by_both_two_nums(lst):
    lst_in_range = lst[55:67]
    result = [num for num in lst_in_range if num % 22 == 0 and num % 82 == 0]
    return result
