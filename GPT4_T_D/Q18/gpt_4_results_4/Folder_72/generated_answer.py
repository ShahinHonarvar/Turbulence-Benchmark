
def sum_ints_div_by_either_nums(lst):
    return sum(num for i, num in enumerate(lst[38:82]) if num % -61 == 0 or num % -71 == 0)
