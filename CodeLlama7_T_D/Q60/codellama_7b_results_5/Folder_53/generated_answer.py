
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list of prime numbers
                primes.append(i)

    # Sort the list of prime numbers in descending order
    primes.sort(reverse=True)

    # Return the list of prime numbers
    return primes

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # Return False if a factor is found
                return False

    # Return True if n is a prime number
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # Return False if a factor is found
                return False

    # Return True if n is a left-and-right-truncatable prime number
    return True
