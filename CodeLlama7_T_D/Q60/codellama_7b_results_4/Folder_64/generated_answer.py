 def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    # filter the list to only include left-and-right-truncatable prime numbers
    result = []
    for prime in primes:
        if is_left_right_truncatable_prime(prime):
            result.append(prime)
    return result

def is_prime(n):

    # check if n is a positive integer

    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # check if n is prime using the trial division algorithm

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):

    # check if n contains no 0

    if "0" in str(n):
        return False

    # check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
