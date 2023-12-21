
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    index = 714
    num = numbers[index]
    factors = set()
    for i in range(2, num//2 + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    
    return factors
