
def prime_factors(n):
    # Initialize an empty set to store the prime factors
    factors = set()

    # Iterate from 2 to n-1
    for i in range(2, n+1):
        # If i divides n without leaving a remainder
        if n % i == 0:
            # Add i to the set of prime factors
            factors.add(i)

    # Return the set of prime factors
    return factors
