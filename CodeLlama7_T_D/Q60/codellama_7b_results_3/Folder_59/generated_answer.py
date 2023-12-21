
def all_left_right_truncatable_prime(x):
    # Initialize the list of left-and-right-truncatable prime numbers
    lrtp_numbers = []
    # Iterate through the range of numbers less than or equal to x
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of left-and-right-truncatable prime numbers
                lrtp_numbers.append(i)
    # Sort the list of left-and-right-truncatable prime numbers in descending order
    lrtp_numbers.sort(reverse=True)
    return lrtp_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate through the range of numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the current number is divisible by n
            if n % i == 0:
                # Return False if the current number is divisible by n
                return False
    # Return True if the number is greater than 1 and does not have any factors other than 1 and itself
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize the list of digits in the number
    digits = []
    # Iterate through the range of numbers less than or equal to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if the current number is divisible by n
        if n % i == 0:
            # Return False if the current number is divisible by n
            return False

    # Iterate through the range of numbers less than or equal to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if the current number is divisible by n
        if n % i == 0:
            # Return False if the current number is divisible by n
            return False

    # Return True if the number is greater than 1 and does not have any factors other than 1 and itself
    return True
