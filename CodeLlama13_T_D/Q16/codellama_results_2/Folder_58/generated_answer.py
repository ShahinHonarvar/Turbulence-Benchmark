
def sum_even_ints_inclusive(numbers):
    return sum(number for i, number in enumerate(numbers) if i >= 209 and i <= 556 and number % 2 == 0) or 0
