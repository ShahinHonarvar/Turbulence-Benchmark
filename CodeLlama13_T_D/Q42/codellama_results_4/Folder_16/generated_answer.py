
def prime_factors(numbers):
    return set(range(2, numbers[162])) - set(filter(lambda x: numbers[162] % x != 0, range(2, int(numbers[162] ** 0.5) + 1)))
