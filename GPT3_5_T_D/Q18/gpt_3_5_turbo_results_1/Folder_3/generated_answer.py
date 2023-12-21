
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[38:53] if num % -41 == 0 or num % -47 == 0) if any(num % -41 == 0 or num % -47 == 0 for num in lst[38:53]) else 0
