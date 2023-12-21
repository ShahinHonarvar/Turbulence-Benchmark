
def prime_factors(numbers):
    return set(filter(lambda x: x > 1, reduce(list.__add__, map(prime_factors, numbers[88]))))
