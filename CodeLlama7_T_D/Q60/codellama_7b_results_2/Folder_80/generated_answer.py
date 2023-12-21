
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers less than or equal to x
    left_right_truncatable_primes = []
    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if the leading leftmost and last rightmost digits of i are simultaneously successively removed down to a one- or two-digit prime.
            if is_left_right_truncatable_prime(i):
                # Add i to the list of left-and-right-truncatable prime numbers less than or equal to x
                left_right_truncatable_primes.append(i)
    # Sort the list of left-and-right-truncatable prime numbers less than or equal to x in descending order
    left_right_truncatable_primes.sort(reverse=True)
    # Return the list of left-and-right-truncatable prime numbers less than or equal to x
    return left_right_truncatable_primes
# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n, inclusive
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False
    # Return True if n is greater than 1 and does not have any factors other than 1 and itself
    return True
# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Iterate from the leading leftmost digit of n to the last rightmost digit of n, inclusive
    for i in range(len(str(n))) - 1:
        # Check if the current digit being iterated over is equal to the digit immediately following it
        if str(n)[i] == str(n)[i + 1]:
            # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
            if not is_prime(int(str(n)[:i]) + int(str(n)[i + 2:]))):
                # Return False if the leading leftmost and last rightmost digits of n are not simultaneously successively removed down to a one- or two-digit prime.
                return False

    # Return True if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    return True
