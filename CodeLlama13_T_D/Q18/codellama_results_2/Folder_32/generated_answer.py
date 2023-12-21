
def sum_ints_div_by_either_nums(numbers):
    return sum([x for x in numbers[25:96] if x % 51 == 0 or x % 77 == 0])
