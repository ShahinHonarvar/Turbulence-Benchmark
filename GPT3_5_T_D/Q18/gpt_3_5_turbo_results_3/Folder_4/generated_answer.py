
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[86:91] if num % -71 == 0 or num % -67 == 0) if any(num % -71 == 0 or num % -67 == 0 for num in lst[86:91]) else 0
