
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[90:98] if num % 13 == 0 or num % 35 == 0) or 0
