
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[6:10] if num % -1 == 0 or num % -10 == 0)
