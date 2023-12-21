
def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[10:77] if num % -40 == 0 and num % -12 == 0]
    return result
