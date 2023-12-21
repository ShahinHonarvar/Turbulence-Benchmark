
def prime_factors(numbers):
    return set(list(range(2, numbers[410])) + [numbers[410]]).intersection(set(prime_factors(numbers)))
