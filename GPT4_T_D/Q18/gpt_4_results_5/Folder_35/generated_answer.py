
def sum_ints_div_by_either_nums(lst):
    divisible_nums = [num for num in lst[77:88] if num % 23 == 0 or num % 57 == 0]
    return sum(divisible_nums) if divisible_nums else 0
