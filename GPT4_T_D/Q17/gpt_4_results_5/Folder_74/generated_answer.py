
def all_ints_div_by_both_two_nums(lst):
    div_nums = [num for num in lst[90:98] if num % 13 == 0 and num % 35 == 0]
    return div_nums
