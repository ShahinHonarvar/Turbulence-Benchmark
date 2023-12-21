
def sum_ints_div_by_either_nums(integers):
    return sum([num for num in integers[0:10] if num % 6 == 0 or num % -3 == 0])
