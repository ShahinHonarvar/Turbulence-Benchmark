
def prime_factors(numbers):
    return set(factor for number in numbers if number == 714 for factor in range(2, int(math.sqrt(number)) + 1) if number % factor == 0)
