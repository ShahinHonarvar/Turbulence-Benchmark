
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = []
        i = 2
        while n > 1:
            if n % i == 0:
                factors.append(i)
                n = n // i
            else:
                i += 1
        return set(factors)

    return get_prime_factors(numbers[10])
