
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a right-truncatable prime number
            if is_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True

# Function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if n is prime
    if not is_prime(n):
        # If n is not prime, it cannot be a right-truncatable prime number
        return False

    # Check if the last rightmost digit of n is equal to 1
    if int(str(n)[-1]) == 1:
        # If the last rightmost digit of n is equal to 1, it cannot be a right-truncatable prime number
        return False

    # Iterate from the second rightmost digit of n to the last rightmost digit of n
    for i in range(len(str(n))) - 2, len(str(n)) - 1:
        # Check if the current digit is equal to 0
        if int(str(n)[i])) == 0:
            # If the current digit is equal to 0, it cannot be a right-truncatable prime number
            return False

    # If all checks are passed, n is a right-truncatable prime number
    return True
