
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Loop through all numbers less than or equal to x
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # Add the prime number to the list
                primes.append(num)

    # Sort the list in descending order
    primes = sorted(primes, reverse=True)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return primes

# Check if a number is a prime number
def is_prime(num):

    # Check if the number is greater than 1
    if num > 1:

        # Loop through all numbers less than the number
        for i in range(2, num):

            # Check if any of the numbers divides the number without a remainder
            if num % i == 0:

                # Return False if any of the numbers divides the number without a remainder
                return False

    # If the number is greater than 1 and all numbers less than the number do not divide it without a remainder, then the number is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(num):

    # Check if the number contains any 0 digits
    for digit in str(num):
        if digit == '0':
            return False

    # Loop through all numbers less than the number
    for i in range(1, num):

        # Check if the number is still prime after removing the leading leftmost and last rightmost digits
        if is_prime(num - i) and is_prime(num + i):

            # Return True if the number is still prime after removing the leading leftmost and last rightmost digits
            return True

    # If none of the numbers less than the number can be removed without making the number non-prime, then the number is not left-and-right-truncatable prime
    return False
