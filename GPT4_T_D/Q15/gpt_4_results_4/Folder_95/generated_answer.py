
def sum_odd_ints_inclusive(numbers):
    return sum(n for i, n in enumerate(numbers[82:87]) if n % 2 != 0)
