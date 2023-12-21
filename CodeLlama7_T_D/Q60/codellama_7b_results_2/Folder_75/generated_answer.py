
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all the numbers from 2 to n - 1
        for i in range(2, n):
            # If n is divisible by i, return False
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n - 1, return True
    return True

# Check if a prime number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
    # Check if n contains the digit 0
    if "0" in str(n):
        return False

    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Loop through all the numbers from 2 to n - 1
    for i in range(2, n):
        # If n is divisible by i, return False
        if n % i == 0:
            return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n - 1, return True
    return True
