
def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [num for num in lst[11:77] if num % -81 == 0 and num % -94 == 0]
    return divisible_by_both
