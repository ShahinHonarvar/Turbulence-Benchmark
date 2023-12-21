
def prime_factors(lst):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
        return factors

    return factors(lst[74])
