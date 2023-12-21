
def sum_ints_div_by_either_nums(lst):
    valid_nums = [num for num in lst[86:91] if num % -71 == 0 or num % -67 == 0]
    return sum(valid_nums) if valid_nums else 0
