
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1, inclusive
        for i in range(2, n):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                # Return False if any such divisor is found
                return False

    # If no divisor is found, return True
    return True

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Check if n contains the digit 0
    if '0' in str(n):
        # Return False if n contains the digit 0
        return False

    # Initialize an empty list to store the digits of n
    digits = []

    # Iterate from left to right and append each digit to the list of digits
    for i in range(len(str(n)))):
        digits.append(str(n))[i])

    # Check if the number of digits in n is odd
    if len(digits) % 2 == 1:
        # Return False if the number of digits in n is odd
        return False

    # Initialize a variable to store the last digit of n
    last_digit = ''

    # Iterate from left to right and remove each digit from the list of digits, starting with the last digit
    for i in range(len(digits)) - 1, -1):
        # Remove the current digit from the list of digits
        digits.pop(i)

        # Check if the remaining digits of n form a prime number
        if is_prime(''.join(map(str, digits)))):
            # If the remaining digits of n form a prime number, return True
            return True

    # If no prime number can be formed by removing digits from n, return False
    return False
