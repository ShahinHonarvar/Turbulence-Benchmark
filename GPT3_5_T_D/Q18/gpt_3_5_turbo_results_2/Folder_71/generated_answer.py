
def sum_ints_div_by_either_nums(integers):
    return sum([num for num in integers[68:100] if num % (-37) == 0 or num % (-26) == 0]) if 68 <= len(integers) <= 99 else 0
