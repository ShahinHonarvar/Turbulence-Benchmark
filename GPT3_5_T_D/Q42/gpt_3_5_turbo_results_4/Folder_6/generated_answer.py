
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = numbers[790]
    factors = set()
    i = 2
    while num > 1:
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            num //= i
        else:
            i += 1
    
    return factors
