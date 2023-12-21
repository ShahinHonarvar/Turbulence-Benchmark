
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers = sorted(prime_numbers)

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If so, return False
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # If so, return False
        if n % i == 0:
            return False

    # If no factors were found, return True
    return True

# Define a function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
    # Check if n contains the digit 0
    if '0' in str(n):
        # If so, return False
        return False

    # Check if n is a palindrome
    if str(n) == str(n)[::-1]:
        # If so, return True
        return True

    # Check if the leading leftmost and last rightmost digits of n are both prime numbers
    if is_prime(int(str(n)[:len(str(n))//2])) and is_prime(int(str(n)[-len(str(n))//2:]))):
        # If so, return True
        return True

    # If no factors were found, return False
    return False
