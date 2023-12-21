
def all_left_right_truncatable_prime(x):
    # List of left-and-right-truncatable prime numbers less than or equal to x
    lrtp = []

    # Iterate from 1 to x

    for i in range(1, x + 1):

        # Check if i is a prime number

        if is_prime(i):

            # Check if i is a left-and-right-truncatable prime number

            if is_left_right_truncatable_prime(i):

                # Add i to the list of left-and-right-truncatable prime numbers

                lrtp.append(i)

    # Sort the list of left-and-right-truncatable prime numbers in ascending order

    lrtp.sort()

    # Return the list of left-and-right-truncatable prime numbers

    return lrtp


def is_prime(n):

    # Check if n is an integer greater than 1

    if not isinstance(n, int) or n < 2:

        return False


    # Check if n is divisible by any integer between 2 and the square root of n

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    # If n is greater than 1, it is prime

    return True


def is_left_right_truncatable_prime(n):

    # Check if n is a left-and-right-truncatable prime number

    if not is_prime(n):

        return False


    # Check if the leading leftmost digit of n is equal to the last rightmost digit of n

    if str(n)[0] != str(n)[-1]:

        return False


    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number

    for i in range(len(str(n)) - 2, -1, -1):

        if not is_prime(int(str(n)[:i] + str(n)[i+1:]))) and len(str(n)[:i] + str(n)[i+1:])) == 1 or 2:

            return False


    # If n is a left-and-right-truncatable prime number, it satisfies the required conditions

    return True
