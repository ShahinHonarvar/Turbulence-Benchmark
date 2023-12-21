
def sum_odd_ints_inclusive(numbers):
    return sum(num for i, num in enumerate(numbers[28:41]) if num % 2)
