
def prime_factors(numbers):
    return set(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), numbers[66]))
