
def sum_ints_div_by_either_nums(integers):
    return sum(num for i, num in enumerate(integers[32:100]) if num % -11 == 0 or num % -15 == 0)
