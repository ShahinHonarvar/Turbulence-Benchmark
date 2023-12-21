
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x (inclusive)
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the leading leftmost and last rightmost digits of i are simultaneously successively removed down to a one- or two-digit prime.
            if is_left_right_truncatable_prime(i):
                # Add the left-and-right-truncatable prime number to the list
                prime_numbers.append(i)

    # Sort the list in descending order and return it
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1 without finding any factors other than 1 and itself
    for i in range(2, n):
        if n % i == 0:
            return False

    # If n is a prime number, it is greater than 1
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    if not is_prime(n % 10) or not is_prime(n // 10)):
        return False

    # If n is a left-and-right-truncatable prime number, it is greater than 1
    return True
