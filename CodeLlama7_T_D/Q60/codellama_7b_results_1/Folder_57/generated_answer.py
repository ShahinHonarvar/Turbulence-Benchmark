
def all_left_right_truncatable_prime(x):
    # Create a list of all left-and-right-truncatable prime numbers less than or equal to x
    left_right_truncatable_primes = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of left-and-right-truncatable prime numbers
                left_right_truncatable_primes.append(i)
    # Sort the list in descending order
    left_right_truncatable_primes.sort(reverse=True)
    # Return the list of left-and-right-truncatable prime numbers
    return left_right_truncatable_primes
# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize variables to keep track of the leading and trailing digits of n
    leading_digits = 0
    trailing_digits = 0

    # Check if the number contains no 0
    if '0' in str(n):
        # Return False if the number contains a 0
        return False

    # Iterate from the last digit of n to the first digit of n
    for i in range(len(str(n)))):
        # Check if the current digit is not equal to the leading digit
        if str(n)[i] != str(leading_digits):
            # Return False if the current digit is not equal to the leading digit
            return False

    # Iterate from the first digit of n to the last digit of n
    for i in range(len(str(n)))):
        # Check if the current digit is not equal to the trailing digit
        if str(n)[i] != str(trailing_digits)):
            # Return False if the current digit is not equal to the trailing digit
            return False

    # Return True if the number is a left-and-right-truncatable prime number
    return True
