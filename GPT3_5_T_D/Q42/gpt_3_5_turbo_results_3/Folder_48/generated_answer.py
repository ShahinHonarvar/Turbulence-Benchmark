
def prime_factors(numbers):
    n = numbers[247]
    factors = set()
    
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    
    if n > 1:
        factors.add(n)
    
    return factors
