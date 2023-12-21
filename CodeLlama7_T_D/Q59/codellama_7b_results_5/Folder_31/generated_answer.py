
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through the tuple and check if each number is prime
    for i in range(len(tuple)):
        num = tuple[i]
        if is_prime(num) and is_left_truncatable_prime(num):
            prime_numbers.append(num)

    # Return the list of all left-truncatable prime numbers less than x, sorted in descending order
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If i divides n without leaving a remainder, then n is not prime
            if n % i == 0:
                return False

    # If the loop completes, then n is prime
    return True

# Define a function to check if a number is left-truncatable prime
def is_left_truncatable_prime(n):
    # Check if n is greater than 1 and if it contains no 0
    if n > 1 and "0" not in str(n):
        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If i divides n without leaving a remainder, then n is not left-truncatable prime
            if n % i == 0:
                return False

    # If the loop completes, then n is left-truncatable prime
    return True
