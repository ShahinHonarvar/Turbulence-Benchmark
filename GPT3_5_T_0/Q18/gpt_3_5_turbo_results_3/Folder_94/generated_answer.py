
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[93:95] if num % -53 == 0 or num % -91 == 0) if len(lst) >= 95 else 0
