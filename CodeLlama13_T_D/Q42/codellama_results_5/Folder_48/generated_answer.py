
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()
    
    i = numbers[247]
    factors = set([1])
    for p in range(2, int(i**0.5) + 1):
        if i % p == 0:
            factors.add(p)
            while i % p == 0:
                i //= p
    
    return factors
