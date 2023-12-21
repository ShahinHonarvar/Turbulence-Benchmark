 def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Iterate from 2 to n-1 (excluding n)
    for i in range(2, n):
        # Check if i is a prime number
        if is_prime(i):
            # Store i in the list of prime numbers
            primes.append(i)
    return sorted(primes)
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1 (excluding n)
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If we reach this point, then n is prime
    return True
