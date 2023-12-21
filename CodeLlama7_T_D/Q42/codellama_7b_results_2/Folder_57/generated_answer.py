
def prime_factors(n):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    
    # Loop through all the prime numbers less than or equal to n
    for p in range(2, int(n ** 0.5) + 1):
        
        # If n is divisible by p, add p to the set of prime factors and continue looping
        if n % p == 0:
            prime_factors.add(p)
    return prime_factors
