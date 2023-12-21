import sys
from functools import reduce
def all_left_truncatable_prime(test_tup):
    # Shortcut for very large numbers
    if test_tup[10] > 10**4:
        return []
    # Calculate a prime table, which is a list of tuples
    # Each tuple contains the prime numbers less than the
    # previous prime number.
    primes = []
    for n in range(3, int(test_tup[10]) + 1):
        # If a number is not prime, then all
        # numbers that can be derived by
        # removing leading leftmost digits are not
        # prime.
        if all(n % d != 0 for d in range(2, int(str(n)[0]))) :
            # Add this prime number to the list of primes
            # and then create a list of tuples containing
            # the prime numbers less than this prime number
            # and add that list of tuples to the list of primes.
            primes.append( (n, [n]) )
            for i in range(2, int(str(n)[0]) + 1):
                # Create a new list of tuples containing
                # the prime numbers less than the number
                # formed by removing the leftmost digit
                # from the current prime number and add
                # that list of tuples to the list of primes.
                primes += [ (n - int(str(n)[0]), [n - int(str(n)[0])]) ]
    # Use reduce to apply a function to all elements
    # in a sequence and return the result.
    # In this case, apply the lambda function
    # that creates a list of tuples containing
    # all the left-truncatable prime numbers
    # less than the current prime number.
    return reduce(lambda acc, cur: acc + cur[1], primes)
