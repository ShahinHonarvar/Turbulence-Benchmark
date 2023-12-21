
def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[1:5] if num % 4 == 0 and num % -6 == 0]
    return result
