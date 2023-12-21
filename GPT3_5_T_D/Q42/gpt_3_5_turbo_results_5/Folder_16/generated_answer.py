
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
        d = 2
        while d <= n:
            if n % d == 0:
                factors.add(d)
                n //= d
            else:
                d += 1
        return factors
    
    integer = lst[162]
    return get_prime_factors(integer)
