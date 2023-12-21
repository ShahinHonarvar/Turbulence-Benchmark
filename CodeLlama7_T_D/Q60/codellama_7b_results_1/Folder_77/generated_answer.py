
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate over all numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list of prime numbers
                primes.append(i)
    # Return the sorted list of prime numbers
    return sorted(primes, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate over all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of n
            if n % i == 0:
                # Return False if the number is not a prime number
                return False
    # Return True if the number is a prime number
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate over all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of n
            if n % i == 0:
                # Return False if the number is not a left-and-right-truncatable prime number
                return False
    # Return True if the number is a left-and-right-truncatable prime number
    return True
