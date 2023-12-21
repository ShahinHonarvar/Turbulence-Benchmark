
def prime_factors(numbers):
    return set(filter(lambda x: x > 1, reduce(lambda a, b: a*b, numbers)))
