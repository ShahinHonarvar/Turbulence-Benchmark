
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x - 1
    for i in range(1, x):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-truncatable prime number
            if is_left_truncatable_prime(i):
                prime_numbers.append(i)

    # Return the list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:
                return False

    # If we reach here, then it is a prime number
    return True

# Function to check if a number is left-truncatable prime number
def is_left_truncatable_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:
                return False

    # If we reach here, then it is a left-truncatable prime number
    return True
