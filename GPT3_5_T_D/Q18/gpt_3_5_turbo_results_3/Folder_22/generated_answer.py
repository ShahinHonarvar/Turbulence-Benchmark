
def sum_ints_div_by_either_nums(integers):
    return sum([num for num in integers[40:201] if num % 21 == 0 or num % 71 == 0])
