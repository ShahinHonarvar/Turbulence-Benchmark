
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):
                # If i is both a prime number and left-and-right-truncatable, add it to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If n is less than or equal to 1, it is not a prime number
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by any number between 2 and the square root of n, it is not a prime number
        if n % i == 0:
            return False

    # If n is greater than 1 and is not divisible by any number between 2 and the square root of n, it is a prime number
    return True

# Define a function to check if a number is left-and-right-truncatable
def is_left_right_truncatable(n):
    # Check if n contains any 0 digits
    if "0" in str(n):
        # If n contains any 0 digits, it is not left-and-right-truncatable
        return False

    # Check if the leading leftmost and last rightmost digits of n are both prime numbers
    if is_prime(int(str(n)[1:])) and is_prime(int(str(n)[:-1])):
        # If the leading leftmost and last rightmost digits of n are both prime numbers, it is left-and-right-truncatable
        return True

    # If the leading leftmost and last rightmost digits of n are not both prime numbers, it is not left-and-right-truncatable
    return False
