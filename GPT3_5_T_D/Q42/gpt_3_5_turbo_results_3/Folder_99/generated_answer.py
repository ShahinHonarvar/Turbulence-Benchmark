
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        return factors

    num = lst[733]
    factors = get_factors(num)
    prime_factors = set()
    for factor in factors:
        if is_prime(factor):
            prime_factors.add(factor)
    return prime_factors
