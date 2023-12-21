
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[13:19] if num % 45 == 0 or num % 20 == 0) if len(lst) > 18 else 0
