
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

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # Return False if n is less than or equal to 1
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # Check if n is divisible by i
        if n % i == 0:
            # Return False if n is divisible by i
            return False

    # Return True if n is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize variables to store the leading and trailing digits of the number
    leading_digit = None
    trailing_digit = None

    # Check if the number has more than one digit
    if len(str(n)) > 1:
        # Get the leading digit of the number
        leading_digit = int(str(n)[0]))
        # Get the trailing digit of the number
        trailing_digit = int(str(n)[-1]))

    # Check if the number has only one digit
    else:
        # Set the leading and trailing digits to the same value as the number
        leading_digit = int(str(n))[0])
        trailing_digit = int(str(n))[0])

    # Check if the leading and trailing digits are not equal
    if leading_digit != trailing_digit:
        # Return False if the leading and trailing digits are not equal
        return False

    # Check if the number is a prime number
    if is_prime(n):
        # Return True if the number is a prime number
        return True

    # Return False if the number is not a prime number
    return False
