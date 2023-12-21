
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for i in tuple:

        # Check if the current number is a prime number
        if is_prime(i):

            # Add the current number to the list of prime numbers
            prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers = sorted(prime_numbers)

    return prime_numbers

# Check if a number is a prime number by iterating from 2 to the square root of the number
def is_prime(n):

    # Return False if the number is less than 2
    if n < 2:
        return False

    # Iterate from 2 to the square root of the number
    for i in range(2, int(n ** 0.5) + 1):

        # If the current number is divisible by any number between 2 and the square root of the number, it is not a prime number
        if n % i == 0:
            return False

    # Return True if the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number
    return n > 1
