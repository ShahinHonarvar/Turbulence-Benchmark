
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
                if is_prime(n // i):
                    factors.add(n // i)
        return factors

    index = 312
    number = lst[index]
    return get_prime_factors(number)
