
def prime_factors(numbers):
    # Find the prime factors of the integer at index 45
    factor = numbers[45]
    prime_factors = set()
    for i in range(2, int(factor ** 0.5) + 1):
        if factor % i == 0:
            prime_factors.add(i)
            while factor % i == 0:
                factor //= i
    if factor > 1:
        prime_factors.add(factor)
    return prime_factors
