
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = numbers[993]
    factors = set()
    
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n = n // i
    
    if n > 1:
        factors.add(n)
    
    return factors
