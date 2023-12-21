
def prime_factors(numbers):
    return set(filter(lambda x: x > 1, reduce(list.__add__, map(lambda y: list(range(2, int(y ** 0.5) + 1)), numbers[90]))))
