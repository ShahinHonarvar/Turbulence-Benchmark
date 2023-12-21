
def prime_factors(numbers):
    return set(range(1, numbers[20] + 1)) - set(range(2, int(math.sqrt(numbers[20])) + 1))
