
def sum_odd_ints_inclusive(numbers):
    return sum(n for i, n in enumerate(numbers[31:73]) if n % 2 != 0)
