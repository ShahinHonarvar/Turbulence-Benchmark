
def sum_ints_div_by_either_nums(lst):
    suitable_nums = [num for num in lst[29:46] if num % 27 == 0 or num % 81 == 0]
    return sum(suitable_nums) if suitable_nums else 0
