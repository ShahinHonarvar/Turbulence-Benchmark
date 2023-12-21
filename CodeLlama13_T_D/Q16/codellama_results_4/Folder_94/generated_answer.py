
def sum_even_ints_inclusive(numbers):
    return sum(filter(lambda x: x % 2 == 0 and 28 <= x <= 40, numbers))
