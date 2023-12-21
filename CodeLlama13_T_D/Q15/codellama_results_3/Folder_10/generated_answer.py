
def sum_odd_ints_inclusive(numbers):
    return sum(filter(lambda x: (x % 2 == 1) and (25 <= x <= 59), numbers))
