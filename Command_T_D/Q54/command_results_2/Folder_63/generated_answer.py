import itertools
def all_right_truncatable_prime(x):
    # If x is 1, return an empty list
    if x[0] == 1:
        return []
    # Create a list of all right-truncatable prime numbers less than x
    right_truncatable_primes = []
    # Iterate through all prime numbers less than x
    for p in itertools.prime_number(x[0]):
        # Check if p is right-truncatable
        # If so, append to the list of right-truncatable primes
        if p % 10 in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89):
            right_truncatable_primes.append(p)
    # Return the sorted list of right-truncatable primes
    return sorted(right_truncatable_primes)
