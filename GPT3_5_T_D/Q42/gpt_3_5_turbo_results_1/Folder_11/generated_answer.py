
def prime_factors(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = lst[77]
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.add(n)
    return factors
