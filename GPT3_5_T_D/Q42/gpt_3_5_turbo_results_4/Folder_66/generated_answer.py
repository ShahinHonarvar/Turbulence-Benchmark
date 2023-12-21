
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = lst[42]
    factors = set()
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            factors.add(i)
    return factors
