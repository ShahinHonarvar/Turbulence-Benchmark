
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[90:201] if num % -31 == 0 or num % 13 == 0) if 90 <= len(lst) <= 200 else 0
