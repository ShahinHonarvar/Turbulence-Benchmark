 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If i is a left-and-right-truncatable prime number, add it to the list of primes
                primes.append(i)
    # Sort the list of primes in descending order
    primes.sort(reverse=True)
    # Return the list of primes
    return primes

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is equal to 1 or 0
    if n == 1 or n == 0:
        # If n is equal to 1 or 0, return False
        return False
    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        # Check if i divides n
        if n % i == 0:
            # If i divides n, return False
            return False

# Define a function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, return False
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(2, int(n ** 0.5) + 1)):
        # Check if i divides n
        if n % i == 0:
            # If i divides n, check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
            if is_prime(n // i):
                # If the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime, return True
                return True

    # If the leading leftmost and last rightmost digits of n are not simultaneously successively removed down to a one- or two-digit prime, return False
    return False
