
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    target_num = numbers[84]
    factors = set()
    for i in range(2, target_num + 1):
        if target_num % i == 0 and is_prime(i):
            factors.add(i)
    return factors
