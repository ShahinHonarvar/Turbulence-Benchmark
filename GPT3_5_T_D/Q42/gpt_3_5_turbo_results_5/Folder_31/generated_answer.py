
def prime_factors(numbers):
    import math
    
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
    num = numbers[66]
    
    factors = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(num // i):
                factors.add(num // i)
    
    return factors
