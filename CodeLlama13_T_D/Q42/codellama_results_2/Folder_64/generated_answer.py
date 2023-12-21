
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()
    
    factors = set()
    for i in range(2, int(numbers[1]) + 1):
        if numbers[1] % i == 0 and is_prime(i):
            factors.add(i)
    
    return factors
