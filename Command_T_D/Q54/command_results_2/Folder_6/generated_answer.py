def all_right_truncatable_prime(x):
    # Convert input to integer
    x = int(x)
    # Find all prime numbers
    primes = []
    # Add all primes
    for i in range(2, x + 1):
        if all(str(i) % j for j in range(2, int(str(i).rstrip('0')) + 1)):
            primes.append(i)
    # Sort and return primes
    return sorted(primes)
