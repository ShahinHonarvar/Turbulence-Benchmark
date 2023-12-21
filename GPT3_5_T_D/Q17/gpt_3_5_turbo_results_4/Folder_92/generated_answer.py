
def all_ints_div_by_both_two_nums(lst):
    return [num for num in lst[:1] if num % 1 == 0 and num % -1 == 0]
