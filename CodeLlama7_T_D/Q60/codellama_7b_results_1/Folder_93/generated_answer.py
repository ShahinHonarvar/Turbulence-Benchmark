
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is prime
def is_prime(n):

    # Check if the number is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):

            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:

                # Return False if the number is divisible by any number between 2 and the square root of the number
                return False

    # If the number is greater than 1, return True if the number is not divisible by any number between 2 and the square root of the number
    return n > 1

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Initialize an empty list to store the digits of the number
    digits = []

    # Iterate from 1 to the length of the number
    for i in range(1, len(str(n))) + 1:

        # Add the digit at position i to the list
        digits.append(int(str(n))[i - 1]))

    # Check if the number is a prime number
    if is_prime(n):

        # Check if the number remains prime after removing the leading leftmost and last rightmost digits
        for i in range(len(digits) - 1):

            # Remove the leading leftmost digit and check if the number remains prime
            if not is_prime(n % int(str(n))[i + 1])):

                # Return False if the number is not a prime number
                return False

    # If the number is a prime number, return True
    return True
