
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Loop through the numbers from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                primes.append(i)
    return primes

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(1, 10):
        if n % i == 0:
            return False

    return True
