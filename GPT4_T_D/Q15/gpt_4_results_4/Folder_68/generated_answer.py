
def sum_odd_ints_inclusive(numbers):
    return sum(num for i, num in enumerate(numbers[:9]) if num % 2 != 0)
