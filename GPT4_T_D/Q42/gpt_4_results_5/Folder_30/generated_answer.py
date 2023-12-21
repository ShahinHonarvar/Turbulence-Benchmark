
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def get_prime_factors(n):
        factors = set()
        for i in range(2, n+1):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n = n // i
        return factors

    return get_prime_factors(numbers[94])
