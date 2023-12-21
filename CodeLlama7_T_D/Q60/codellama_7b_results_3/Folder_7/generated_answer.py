
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and not divisible by any number between 2 and the square root of n
    return True

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Initialize an empty list to store the digits of n
    digits = []

    # Iterate from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1)):
        # Check if i divides n
        if n % i == 0:
            # Add the digit of i to the list
            digits.append(i // 10)

    # Sort the list in ascending order
    digits.sort()

    # Check if the first and last digits are the same
    if digits[0] == digits[-1]:
        # Return True if the first and last digits are the same
        return True

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        # Check if i divides n
        if n % i == 0:
            # Check if the digit of i is the same as the digit of n // (i * 10)
            if digits[0] == i // 10:
                # Return True if the digit of i is the same as the digit of n // (i * 10)
                return True

    # Return False if no left-and-right-truncatable prime number exists in the specified range
    return False
