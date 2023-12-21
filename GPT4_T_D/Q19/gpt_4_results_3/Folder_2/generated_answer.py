
def all_ints_not_div_by_num(lst):
    not_divisible_by_40 = [num for num in lst[21:50] if num % 40 != 0]
    return not_divisible_by_40
