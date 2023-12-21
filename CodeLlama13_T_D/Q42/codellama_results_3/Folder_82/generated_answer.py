
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()
    
    num = numbers[83]
    factors = set([])
    
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
            
    if num > 1:
        factors.add(num)
    
    return factors
