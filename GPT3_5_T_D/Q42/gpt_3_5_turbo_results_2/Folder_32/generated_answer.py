
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    integer = numbers[849]
    factors = set()
    for i in range(2, integer + 1):
        if integer % i == 0 and is_prime(i):
            factors.add(i)
    return factors
