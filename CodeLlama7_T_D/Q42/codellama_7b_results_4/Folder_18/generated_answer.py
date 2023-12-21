
def prime_factors(n):
    # Initialize a set to store the prime factors
    factors = set()

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If i divides n, add it to the set of prime factors
        if n % i == 0:
            factors.add(i)

    # Return the set of prime factors
    return factors
