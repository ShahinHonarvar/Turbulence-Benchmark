
def prime_factors(numbers):
    return set([x for x in range(2, 100) if all(y % x == 0 for y in numbers)])
