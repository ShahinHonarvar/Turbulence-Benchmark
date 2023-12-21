
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[7:10] if num % 2 == 0 or num % 3 == 0) if len(lst) >= 10 and any(num % 2 == 0 or num % 3 == 0 for num in lst[7:10]) else 0
