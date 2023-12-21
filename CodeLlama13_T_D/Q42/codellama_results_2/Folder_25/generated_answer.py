
def prime_factors(numbers):
    return set(filter(lambda x: x > 1, reduce(operator.mul, numbers[90:])))
