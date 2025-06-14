
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers = sorted(prime_numbers)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:
                # Return False if the number is divisible by any number between 2 and the square root of the number
                return False

    # Return True if the number is greater than 1 and not divisible by any number between 2 and the square root of the number
    return n > 1

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize a variable to store the number
    num = n

    # Remove the leading leftmost digit of the number
    num = int(str(num)[1:])

    # Check if the number is still a prime number
    if not is_prime(num):
        # Return False if the number is not still a prime number
        return False

    # Remove the last rightmost digit of the number
    num = int(str(num)[:-1]))

    # Check if the number is still a prime number
    if not is_prime(num):
        # Return False if the number is not still a prime number
        return False

    # Return True if the number is still a prime number after removing both the leading leftmost and last rightmost digits
    return True
