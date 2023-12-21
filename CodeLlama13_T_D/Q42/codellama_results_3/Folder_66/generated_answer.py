
def prime_factors(numbers):
    return set([n for n in range(1, numbers[42]) if all(numbers[42] % i != 0 for i in range(1, int(n ** 0.5) + 1))])
