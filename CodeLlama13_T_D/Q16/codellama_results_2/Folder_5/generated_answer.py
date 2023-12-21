
def sum_even_ints_inclusive(numbers):
    return sum(filter(lambda x: (x % 2 == 0) and (8 <= x <= 9), numbers))
