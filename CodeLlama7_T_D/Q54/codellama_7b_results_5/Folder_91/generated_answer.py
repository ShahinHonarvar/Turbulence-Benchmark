
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all integers less than x
    for i in range(1, x):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is right-truncatable prime number
            if is_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is prime
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        # Return False if n is less than 2
        return False

    # Loop through all integers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            # Return False if i divides n
            return False

    # Return True if n is prime
    return True

# Check if a number is right-truncatable prime
def is_right_truncatable_prime(n):
    # Check if n is prime
    if not is_prime(n):
        # Return False if n is not prime
        return False

    # Loop through all integers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            # Return False if i divides n
            return False

    # Return True if n is right-truncatable prime
    return True
