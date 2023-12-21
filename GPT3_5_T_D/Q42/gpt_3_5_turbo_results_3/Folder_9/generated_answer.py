
def prime_factors(numbers):
    """Return the set of prime factors of the integer at index 24 in the given list."""
    number = numbers[24]
    factors = set()
    i = 2
    while number > 1:
        if number % i == 0:
            factors.add(i)
            number //= i
        else:
            i += 1
    return factors
