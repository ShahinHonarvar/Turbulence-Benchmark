
def sum_odd_ints_inclusive(numbers):
    return sum(n for i, n in enumerate(numbers[90:201]) if n % 2 != 0)
