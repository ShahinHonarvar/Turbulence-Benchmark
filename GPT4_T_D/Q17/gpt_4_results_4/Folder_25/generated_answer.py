
def all_ints_div_by_both_two_nums(lst):
    ints_div_by_both = [num for num in lst[25:81] if num % -20 == 0 and num % -26 == 0]
    return ints_div_by_both
