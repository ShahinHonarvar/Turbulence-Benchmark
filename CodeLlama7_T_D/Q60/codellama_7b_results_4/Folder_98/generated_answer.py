 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Loop through all numbers less than or equal to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                primes.append(i)
    # Sort the list in descending order
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n < 2:
        return False

def is_left_right_truncatable_prime(n):
    # Check if the number contains no 0
    if '0' in str(n):
        return False
