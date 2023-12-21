
def prime_factors(lst):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = lst[162]
    factors = set()
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(n // i):
                factors.add(n // i)
    
    return factors
