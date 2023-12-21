
def sum_ints_div_by_either_nums(lst):
    divisible_ints = [num for num in lst[10:101] if num % 10 == 0 or num % 100 == 0]
    return sum(divisible_ints) if len(divisible_ints) > 0 else 0
