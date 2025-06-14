
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
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # Return False if n is less than or equal to 1
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        # If n is divisible by i, it is not a prime number
        if n % i == 0:
            # Return False if n is divisible by any number between 2 and n-1
            return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n-1, it is a prime number
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize variables to store the digits of n
    leftmost = 0
    rightmost = 0

    # Extract the digits of n from left to right
    for digit in str(n):
        # If this is the first digit, make it the leftmost digit
        if leftmost == 0:
            leftmost = int(digit)

        # Add the current digit to the list of digits
        rightmost = int(digit)

    # Initialize variables to store the prime numbers
    left_prime_numbers = []
    right_prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, n + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-truncatable prime number
            if is_left_truncatable_prime(i, leftmost)):
                # Add the prime number to the list of left-truncatable prime numbers
                left_prime_numbers.append(i)

            # Check if the number is right-truncatable prime number
            if is_right_truncatable_prime(i, rightmost)):
                # Add the prime number to the list of right-truncatable prime numbers
                right_prime_numbers.append(i)

    # Check if there are any left-truncatable prime numbers that remain prime when the leading leftmost digit is removed
    for left_prime_number in left_prime_numbers:
        # If the left-truncatable prime number remains prime when the leading leftmost digit is removed, it is a left-and-right-truncatable prime number
        if is_left_truncatable_prime(left_prime_number, leftmost)):
            # Return True if there are any left-truncatable prime numbers that remain prime when the leading leftmost digit is removed
            return True

    # Check if there are any right-truncatable prime numbers that remain prime when the last rightmost digit is removed
    for right_prime_number in right_prime_numbers:
        # If the right-truncatable prime number remains prime when the last rightmost digit is removed, it is a left-and-right-truncatable prime number
        if is_right_truncatable_prime(right_prime_number, rightmost)):
            # Return True if there are any right-truncatable prime numbers that remain prime when the last rightmost digit is removed
            return True

    # Check if there are any left-and-right-truncatable prime numbers in the list of prime numbers
    for prime_number in range(1, n + 1):
        # If the current prime number is a left-and-right-truncatable prime number, it is not a prime number and the loop continues
        if (not is_left_truncatable_prime(prime_number, leftmost)) and \
                (not is_right_truncatable_prime(prime_number, rightmost))):
            # Return False if there are no left-and-right-truncatable prime numbers in the list of prime numbers
            return False

    # If there are any left-and-right-truncatable prime numbers in the list of prime numbers, it is a prime number and the loop continues
    return True
