
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # filter the list to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = []
    for prime in prime_numbers:
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_prime_numbers.append(prime)
    return sorted(left_right_truncatable_prime_numbers, reverse=True)
def is_left_right_truncatable_prime(n):
    # check if n is a prime number
    if not is_prime(n):
        return False

    # check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, 10):
        if is_prime(int(str(n)[:i])) and is_prime(int(str(n)[-i:])):
            return True

    # if no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
    return False

def is_prime(n):

    # check if n is greater than 1

    if n > 1:

        # check if n is a multiple of 2 to 10

        for i in range(2, 11):
            if n % i == 0:
                return False

        # if n is a prime number, it should have no prime factors other than itself and 1

        if prime_factors(n) == [1, n]:
            return True

    # if n is not a prime number, the function should return False

    return False

def prime_factors(n):

    # create an empty list to store the prime factors of n

    prime_factors = []

    # check if n is equal to 1

    if n == 1:

        # if n is equal to 1, it should have no prime factors other than itself and 1

        return [1, n]

    # check if n is even

    if n % 2 == 0:

        # if n is even, it should have a prime factor of 2

        prime_factors.append(2)

    # check if n is odd

    if n % 2 != 0:

        # if n is odd, it should have a prime factor that is one more than a multiple of 3

        for i in range(1, int((n - 1) / 3) + 1):
            if n - 3 * i == 1 or is_prime(n - 3 * i):
                prime_factors.append(n - 3 * i)

    # return the list of prime factors of n, sorted in descending order

    return sorted(prime_factors, reverse=True)
