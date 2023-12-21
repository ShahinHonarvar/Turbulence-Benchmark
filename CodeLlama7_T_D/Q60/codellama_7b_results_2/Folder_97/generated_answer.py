
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):

    # Check if the number is greater than 1
    if n > 1:

        # Loop through all numbers from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):

            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:

                # Return False if the number is divisible by any number between 2 and the square root of the number
                return False

    # Return True if the number is greater than 1 and not divisible by any number between 2 and the square root of the number
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains 0
    if '0' in str(n):

        # Return False if the number contains 0
        return False

    # Loop through all numbers from 1 to the square root of the number
    for i in range(1, int(n ** 0.5) + 1):

        # Check if the number is divisible by any number between 1 and the square root of the number
        if n % i == 0:

            # Return False if the number is divisible by any number between 1 and the square root of the number
            return False

    # Return True if the number is greater than 1 and not divisible by any number between 1 and the square root of the number
    return True
