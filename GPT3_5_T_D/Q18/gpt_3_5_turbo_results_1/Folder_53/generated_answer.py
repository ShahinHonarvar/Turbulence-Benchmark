
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[200:201] if num % 17 == 0 or num % -5 == 0) or 0
