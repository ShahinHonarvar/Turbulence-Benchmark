
def all_left_truncatable_prime(x):
    """
    Returns a list of all left-truncatable prime numbers less than x, sorted in descending order.
    """

    # create a set to store the prime numbers
    primes = set()

    # iterate over the numbers from 1 to x - 1
    for i in range(1, x):

        # check if the number is a prime number
        if is_prime(i):

            # add the prime number to the set
            primes.add(i)

    # create an empty list to store the left-truncatable prime numbers
    ltprimes = []

    # iterate over the prime numbers in the set
    for i in primes:

        # check if the number is a left-truncatable prime number
        if is_left_truncatable_prime(i):

            # add the left-truncatable prime number to the list
            ltprimes.append(i)

    # sort the list of left-truncatable prime numbers in descending order
    ltprimes.sort(reverse=True)

    # return the list of left-truncatable prime numbers
    return ltprimes

def is_prime(n):

    """
    Returns True if n is a prime number, False otherwise.
    """

    # check if n is less than or equal to 1
    if n <= 1:

        # n is not a prime number
        return False

    # check if n is divisible by 2 to n - 1
    for i in range(2, n):

        # check if i divides n
        if n % i == 0:

            # n is not a prime number
            return False

    # n is a prime number
    return True

def is_left_truncatable_prime(n):

    """
    Returns True if n is a left-truncatable prime number, False otherwise.
    """

    # check if n is less than or equal to 1
    if n <= 1:

        # n is not a left-truncatable prime number
        return False

    # check if the leading leftmost digit of n is successively removed, then all resulting numbers are prime
    for i in range(len(str(n))))):

        # remove the leading leftmost digit of n
        n = int(str(n)[1:]))

        # check if n is a prime number
        if not is_prime(n):

            # n is not a left-truncatable prime number
            return False

    # n is a left-truncatable prime number
    return True
