
def sum_even_ints_inclusive(numbers):
    return sum(number for i, number in enumerate(numbers) if 22 <= i <= 50 and number % 2 == 0) or 0
