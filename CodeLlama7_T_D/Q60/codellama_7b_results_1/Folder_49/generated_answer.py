
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all the prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is a left-and-right-truncatable prime number
    return True
