
def sum_ints_div_by_either_nums(lst):
    sum_divisible = sum(i for i in lst[48:60] if i % 88 == 0 or i % 58 == 0)
    return sum_divisible if sum_divisible else 0
