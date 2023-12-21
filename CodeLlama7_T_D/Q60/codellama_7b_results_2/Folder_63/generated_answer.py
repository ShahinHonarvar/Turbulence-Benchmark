
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_list.append(i)

    return prime_list

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is prime
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is greater than 1 and it contains no 0
    if n > 1 and '0' not in str(n):
        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not left-and-right-truncatable prime number
                return False

        # Loop through all numbers from the square root of n to the square root of n
        for i in range(int(n ** 0.5)), int(n ** 0.5)):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not left-and-right-truncatable prime number
                return False

    # If n is greater than 1 and it contains no 0 and it is not divisible by any number between 2 and the square root of n, then it is left-and-right-truncatable prime number
    return True
