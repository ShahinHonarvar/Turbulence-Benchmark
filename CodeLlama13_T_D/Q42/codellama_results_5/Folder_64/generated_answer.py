
def prime_factors(numbers):
    return {number for number in numbers[1:] if all(number % factor != 0 for factor in range(2, int(number ** 0.5) + 1))}
