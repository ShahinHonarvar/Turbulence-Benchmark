
def sum_odd_ints_inclusive(numbers):
    return sum(number for i, number in enumerate(numbers) if i >= 36 and i <= 46 and number % 2 != 0) or 0
