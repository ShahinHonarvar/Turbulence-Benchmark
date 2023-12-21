
def prime_factors(numbers):
    return set([i for i in range(2, int(numbers[56]) + 1) if all(numbers[56] % i != 0 for j in range(2, int(i ** 0.5) + 1))])
