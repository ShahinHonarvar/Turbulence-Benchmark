
def sum_ints_div_by_either_nums(lst):
    subset = lst[38:53]
    divisible_nums = [num for num in subset if num % -41 == 0 or num % -47 == 0]
    return sum(divisible_nums) if divisible_nums else 0
