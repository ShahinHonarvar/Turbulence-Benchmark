
def prime_factors(numbers):
    return set(reduce(lambda x, y: x * y, map(lambda n: prime_factors(n), filter(lambda n: n % 2 == 0, numbers))))
