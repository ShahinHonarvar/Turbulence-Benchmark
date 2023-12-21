
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number using the Sieve of Eratosthenes
        if is_prime(i):

            # Check if the number can be obtained by successively removing the leftmost and rightmost digits
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number using the Sieve of Eratosthenes
def is_prime(n):

    # Initialize a boolean variable to store the result
    is_prime = True

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        # Check if n is divisible by i
        if n % i == 0:

            # If it is, set is_prime to False and break out of the loop
            is_prime = False
            break

    # Return the result
    return is_prime

# Check if a number can be obtained by successively removing the leftmost and rightmost digits
def is_left_right_truncatable_prime(n):

    # Initialize variables to store the leading digit and the last rightmost digit of n
    leading_digit = 0
    last_rightmost_digit = 0

    # Check if n contains any zero digits
    if '0' in str(n):

        # If it does, return False since a prime number cannot contain any zero digits
        return False

    # Get the leading digit of n
    for char in str(n):

        # If the character is not a zero digit, set leading_digit to its value and break out of the loop
        if char != '0':
            leading_digit = int(char)
            break

    # Get the last rightmost digit of n
    for i in range(len(str(n)))):

        # If the character at index i is not a zero digit, set last_rightmost_digit to its value and break out of the loop
        if str(n)[i] != '0':
            last_rightmost_digit = int(str(n)[i]))
            break

    # Check if leading_digit is equal to 1 or last_rightmost_digit is equal to 1
    if leading_digit == 1 or last_rightmost_digit == 1:

        # If it is, return False since a prime number cannot have any leading zeros or trailing zeros
        return False

    # Get the prime factors of n
    prime_factors = get_prime_factors(n)

    # Check if any of the prime factors are equal to 1 or last_rightmost_digit is equal to 1
    for factor in prime_factors:

        # If any of the prime factors are equal to 1, return False since a prime number cannot have any leading zeros or trailing zeros
        if factor == 1 or last_rightmost_digit == 1:
            return False

    # Return True since all checks have passed
    return True

# Get the prime factors of a number using the Euclidean algorithm
def get_prime_factors(n):

    # Initialize an empty list to store the prime factors
    prime_factors = []

    # Initialize a variable to store the remainder
    remainder = n

    # Iterate from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):

        # Check if the number is divisible by i using the modulo operator
        while remainder % i == 0:

            # If it is, add i to the list of prime factors and update the remainder accordingly
            prime_factors.append(i)
            remainder = remainder // i

    # Return the list of prime factors
    return prime_factors
