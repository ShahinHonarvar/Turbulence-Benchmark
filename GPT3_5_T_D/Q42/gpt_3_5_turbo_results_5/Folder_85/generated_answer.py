
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = lst[23]
    factors = set()
    
    if is_prime(num):
        factors.add(num)
    
    for i in range(2, int(num // 2) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    
    return factors
