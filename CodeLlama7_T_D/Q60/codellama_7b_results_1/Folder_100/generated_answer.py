
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Create an empty list to store the left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = []
    # Iterate over the prime numbers and check if they are left-and-right-truncatable prime numbers
    for prime in prime_numbers:
        # Check if the number is a prime number
        if is_prime(prime):
            # Check if the number contains no 0
            if not '0' in str(prime):
                # Create a list of all the left-and-right-truncatable prime numbers that are less than or equal to x
                left_right_truncatable_prime_numbers = [p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)]
                # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
                return left_right_truncatable_prime_numbers
    # If no left-and-right-truncatable prime number exists in the specified range, the function should return an empty list.
    return []

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        # If the number is less than or equal to 1, return False
        return False
    # Check if the number is divisible by 2 to n
    for i in range(2, n + 1):
        # Check if the number is divisible by i
        if n % i == 0:
            # If the number is divisible by i, return False
            return False
    # If the number is not divisible by any number between 2 and n, return True
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains no 0
    if not '0' in str(n):
        # Create a list of all the left-and-right-truncatable prime numbers that are less than or equal to n
        left_right_truncatable_prime_numbers = [p for p in range(2, n + 1) if is_left_right_truncatable_prime(p)]
        # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
        return left_right_truncatable_prime_numbers
    # If the number contains no 0, return False
    return False
