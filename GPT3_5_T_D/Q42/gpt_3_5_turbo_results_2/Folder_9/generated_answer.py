
def prime_factors(numbers):
    factor = numbers[24]
    primes = set()
    while factor % 2 == 0:
        primes.add(2)
        factor //= 2
    for i in range(3, int(factor ** 0.5) + 1, 2):
        while factor % i == 0:
            primes.add(i)
            factor //= i
    if factor > 2:
        primes.add(factor)
    return primes
