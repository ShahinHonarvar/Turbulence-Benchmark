
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, checking for each number if it is a left-and-right-truncatable prime number
    for i in range(1, x + 1):

        # Check if the current number is a prime number

        if is_prime(i):

            # Check if the current number is a left-and-right-truncatable prime number

            if is_left_right_truncatable_prime(i):

                # Add the current number to the list of prime numbers

                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order

    prime_numbers.sort()

    # Return the sorted list of prime numbers

    return prime_numbers


def is_prime(n):

    # Check if n is less than or equal to 1

    if n <= 1:

        # If n is less than or equal to 1, it is not a prime number

        return False


    # Check if n is divisible by 2 to n - 1

    for i in range(2, n):

        # If n is divisible by i, it is not a prime number

        if n % i == 0:

            return False


    # If n is greater than 1 and it is not divisible by 2 to n - 1, it is a prime number

    return True


def is_left_right_truncatable_prime(n):

    # Check if n is less than or equal to 1

    if n <= 1:

        # If n is less than or equal to 1, it is not a left-and-right-truncatable prime number

        return False


    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime. If they are, then n is a left-and-right-truncatable prime number.

    for i in range(10):

        # Check if the leading leftmost digit of n is i

        if n // 10 ** (len(str(n))) - 1) % 10 == i:

            # Remove the leading leftmost digit of n

            n = n // 10 ** (len(str(n)))) - 1

    for i in range(10):

        # Check if the last rightmost digit of n is i

        if n % 10 == i:

            # Remove the last rightmost digit of n

            n = n // 10

    # If n is greater than 1 and it is not divisible by 2 to n - 1, it is a left-and-right-truncatable prime number

    return True
