 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of primes
                primes.append(i)
    # Sort the list of primes in ascending order
    primes.sort()
    return primes

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is divisible by 10
    if n % 10 == 0:
        return False

    # Check if the leading leftmost digit of n is equal to the last rightmost digit of n
    if int(str(n)[0]) != int(str(n)[-1])):
        return False

    # Check if the leading leftmost digit of n is not equal to the last rightmost digit of n
    if int(str(n)[0]) == int(str(n)[-1])):
        return True

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

# Define a function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is divisible by 10
    if n % 10 == 0:
        return False

    # Check if the leading leftmost digit of n is equal to the last rightmost digit of n
    if int(str(n)[0]) != int(str(n)[-1])):
        return False

    # Check if the leading leftmost digit of n is not equal to the last rightmost digit of n
    if int(str(n)[0]) == int(str(n)[-1])):
        return True
