
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[41:57] if num % 82 == 0 or num % 90 == 0) if 41 <= len(lst) <= 56 else 0
