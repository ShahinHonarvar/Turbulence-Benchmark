
def sum_ints_div_by_either_nums(lst):
    return sum(num for idx, num in enumerate(lst[1:9]) if num % -9 == 0 or num % -3 == 0)
