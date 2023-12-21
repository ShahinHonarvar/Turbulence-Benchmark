
def sum_ints_div_by_either_nums(integers):
    return sum(num for num in integers[:2] if num % 2 == 0 or num % 1 == 0) if len(integers) >= 2 else 0
