
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[42:88] if num % -90 == 0 or num % -74 == 0) if any(num % -90 == 0 or num % -74 == 0 for num in lst[42:88]) else 0
