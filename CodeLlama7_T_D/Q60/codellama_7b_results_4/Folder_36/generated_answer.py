 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)
    return prime_numbers

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False
    # If n is greater than 1 and there are no divisors other than itself and 1, return True
    return True

def left_right_truncatable_prime(n):
    # Initialize a list to store the digits of n
    digits = []

    # Check if n contains any 0s
    if "0" in str(n):
        # Return False if n contains any 0s
        return False

    # Loop through the digits of n
    for digit in str(n):
        # Append each digit to the list
        digits.append(digit)

    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Check if n is a one-digit prime number
    if len(digits) == 1 and is_prime(int(digits[0])):
        # Return True if n is a one-digit prime number
        return True

    # Check if n is a two-digit prime number
    elif len(digits) == 2 and is_prime(int(digits[0] + digits[1])):
        # Return True if n is a two-digit prime number
        return True

    # If n does not meet the criteria for either one- or two-digit prime numbers, return False
    else:
        return False
