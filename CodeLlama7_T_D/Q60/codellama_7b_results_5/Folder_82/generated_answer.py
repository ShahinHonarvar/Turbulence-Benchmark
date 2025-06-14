
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:

        # Return False if n is less than or equal to 1
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        # Check if n is divisible by i
        if n % i == 0:

            # Return False if n is divisible by any number between 2 and the square root of n
            return False

    # If n is not divisible by any number between 2 and the square root of n, it must be prime
    return True

# Define a function to check if a left-and-right-truncatable prime number exists in the specified range
def is_left_right_truncatable_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:

        # Return False if n is less than or equal to 1
        return False

    # Check if n contains any 0 digits
    if '0' in str(n):

        # Return False if n contains any 0 digits
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        # Check if n is divisible by i
        if n % i == 0:

            # Return False if n is divisible by any number between 2 and the square root of n
            return False

    # If n is not divisible by any number between 2 and the square root of n, it must be prime
    return True
