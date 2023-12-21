
def prime_factors(numbers):
    return set(filter(lambda x: x > 1, map(lambda x: x if x == 1 else x * (x - 1), numbers)))
