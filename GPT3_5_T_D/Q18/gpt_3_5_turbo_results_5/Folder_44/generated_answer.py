
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[25:71] if num % 74 == 0 or num % 15 == 0) or 0
