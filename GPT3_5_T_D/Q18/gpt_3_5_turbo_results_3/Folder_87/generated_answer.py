
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[18:53] if num % 15 == 0 or num % 57 == 0)
