
def sum_ints_div_by_either_nums(lst):
    divisible_ints = [num for num in lst[2:8] if num % -1 == 0 or num % -7 == 0]
    return sum(divisible_ints) if divisible_ints else 0
