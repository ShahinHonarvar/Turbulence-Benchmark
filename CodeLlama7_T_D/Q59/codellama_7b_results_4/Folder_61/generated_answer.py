
def all_left_truncatable_prime(tuple_of_primes):
    # Initialize an empty list for the result
    result = []

    # Iterate over the prime numbers in the tuple
    for prime in tuple_of_primes:
        # If the current prime number is less than x, add it to the result
        if prime < x:
            result.append(prime)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(result, reverse=True)
