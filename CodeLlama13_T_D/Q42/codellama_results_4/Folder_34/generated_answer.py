
def prime_factors(numbers):
    return set(factor for number in numbers if isinstance(number, int) and number > 1 for factor in range(2, int(math.sqrt(number)) + 1) if number % factor == 0)
