
def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the numbers from 1 to n-1
    for i in range(2, n):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is right-truncatable prime number
            if is_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of n
            if n % i == 0:
                # Return False if the number is not prime
                return False

    # Return True if the number is prime
    return True

# Check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if the number is a prime number
    if not is_prime(n):
        # Return False if the number is not a prime number
        return False

    # Loop through the numbers from 2 to n-1
    for i in range(2, n):
        # Check if the number is divisible by any number between 2 and n-1
        if n % i == 0:
            # Return False if the number is not a right-truncatable prime number
            return False

    # Return True if the number is a right-truncatable prime number
    return True
