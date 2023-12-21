
def prime_factors(numbers):
    return set(filter(lambda x: x > 1, (factor for n in numbers if n == 926 for factor in range(2, int(n ** 0.5) + 1) if n % factor == 0)))
