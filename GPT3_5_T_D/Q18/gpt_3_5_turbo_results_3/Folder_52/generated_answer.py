
def sum_ints_div_by_either_nums(lst):
    return sum([num for num in lst[48:60] if num % 88 == 0 or num % 58 == 0]) if any(num % 88 == 0 or num % 58 == 0 for num in lst[48:60]) else 0
