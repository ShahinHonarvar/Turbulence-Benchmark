
def all_right_truncatable_prime(tuple_of_integers):
    # Initialize a list to store the right-truncatable prime numbers
    right_truncatable_primes = []

    # Iterate over the tuple of integers

    for integer in tuple_of_integers:
        if is_right_truncatable_prime(integer):
            right_truncatable_primes.append(integer)

    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(n):

    # Check if n is a prime number

    if not is_prime(n):
        return False

    # Remove the last rightmost digit of n and check if it remains prime

    for i in range(1, len(str(n)))):
        if not is_prime(int(str(n)[:-i])):
            return False

    return True


def is_prime(n):

    # Check if n is an integer greater than 1

    if not isinstance(n, int)) or n < 2:
        return False

    # Check if n has any prime factors other than 2 and 3

    for i in range(2, int(n ** 0.5)) + 1):
        if n % i == 0:
            return False

    return True
