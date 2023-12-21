
def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        if n < 2:
            return factors
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(n**0.5)+1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    
    return get_prime_factors(lst[132])
