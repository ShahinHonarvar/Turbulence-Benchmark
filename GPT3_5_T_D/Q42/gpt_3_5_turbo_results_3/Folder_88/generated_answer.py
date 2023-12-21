

def prime_factors(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    num = lst[46]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
        if num % i == 0 and is_prime(num // i):
            factors.add(num // i)
            
    return factors
