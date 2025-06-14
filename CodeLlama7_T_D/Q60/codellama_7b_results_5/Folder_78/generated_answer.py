
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)
    # Return the list of prime numbers in ascending order
    return sorted(prime_numbers)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n contains any 0
    if '0' in str(n):
        # Return False if n contains any 0
        return False

    # Iterate from the leading leftmost digit to the last rightmost digit
    for i in range(len(str(n)))):
        # Check if removing the leading leftmost digit and the last rightmost digit simultaneously results in a prime number
        if is_prime(int(str(n))[:i] + int(str(n))[i+1:]):
            # Return True if removing the leading leftmost digit and the last rightmost digit simultaneously results in a prime number
            return True
