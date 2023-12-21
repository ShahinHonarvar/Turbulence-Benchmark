
def sum_ints_div_by_either_nums(integers):
    return sum(num for num in integers[1:9] if num % -9 == 0 or num % -3 == 0) if len(integers) >= 9 else 0
