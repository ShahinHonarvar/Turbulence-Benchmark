
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    factor = numbers[78]
    prime_factors = set()
    for i in range(2, factor + 1):
        if factor % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors
