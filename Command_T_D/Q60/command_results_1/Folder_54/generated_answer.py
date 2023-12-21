
def all_left_right_truncatable_prime(n):
    # Sieve of Eratosthenes
    # Create a list of all primes less than or equal to the given integer
    # Use the sieve of Eratosthenes to efficiently create the list
    # Set up the list with all integers from 2 to the given integer
    primes = list(range(2, n + 1))
    # Create a list to store the primes
    primes = []
    # Iterate over all integers
    for p in primes:
        # If the integer is prime, add it to the list
        if all(p % d != 0 for d in range(2, int(p ** .5) + 1)):
            primes.append(p)
    # Return the list of primes
    return sorted(set(primes))
