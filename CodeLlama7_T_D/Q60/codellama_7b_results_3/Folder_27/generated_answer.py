
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x (exclusive)
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers


def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by any number between 2 and n-1
        for i in range(2, n):
            if n % i == 0:
                return False

    return True


def is_left_right_truncatable_prime(n):

    # Check if n contains any digit that is equal to 0
    if '0' in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, len(str(n)))):

        # Check if the current digit is equal to 0
        if str(n)[i] == '0':
            return False

        # Remove the leading leftmost and last rightmost digits of n simultaneously successively removed down to a one- or two-digit prime
        for j in range(i + 1, len(str(n)))):
            if str(n)[j] == '0':
                return False

    return True
