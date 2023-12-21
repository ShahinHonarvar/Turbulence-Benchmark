
def prime_factors(numbers):
    return set(reduce(list.__add__, (factorize(n) for n in numbers)))
