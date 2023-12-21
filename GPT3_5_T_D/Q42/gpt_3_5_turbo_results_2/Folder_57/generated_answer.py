
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    index = 92  # index of the integer we want to find prime factors for
    
    num = numbers[index]
    factors = set()
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            while num % i == 0:
                num = num // i
                factors.add(i)
    
    if num > 1:
        factors.add(num)
    
    return factors
