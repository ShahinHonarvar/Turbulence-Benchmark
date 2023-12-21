
def prime_factors(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        return factors

    return get_factors(numbers[478])
