
def all_left_truncatable_prime(tuple_of_primes):
    # Initialize an empty list to store the results
    left_truncatable_primes = []
    # Iterate over the tuple of prime numbers
    for prime in tuple_of_primes:
        # Check if the prime number is a left-truncatable prime number
        if is_left_truncatable_prime(prime):
            # Add the prime number to the list of left-truncatable prime numbers
            left_truncatable_primes.append(prime)
    # Sort the list of left-truncatable prime numbers in ascending order
    left_truncatable_primes.sort()
    return left_truncatable_primes
