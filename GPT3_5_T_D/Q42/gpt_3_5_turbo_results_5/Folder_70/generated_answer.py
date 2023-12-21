
def prime_factors(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    integer = lst[845]
    factors = set()
    for i in range(2, int(integer**0.5) + 1):
        if integer % i == 0 and is_prime(i):
            factors.add(i)
        if integer % (integer // i) == 0 and is_prime(integer // i):
            factors.add(integer // i)
    return factors
