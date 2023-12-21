
def sum_odd_ints_inclusive(numbers):
    return sum(number for i, number in enumerate(numbers) if i >= 91 and i <= 99 and number % 2 != 0)
