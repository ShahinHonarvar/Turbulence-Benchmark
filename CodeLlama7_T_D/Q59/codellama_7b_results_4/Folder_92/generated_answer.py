
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for num in tuple:
        # Check if the number is a prime number
        if is_prime(num):
            # Add the prime number to the list
            prime_numbers.append(num)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:
                # If it is divisible, return False
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number, then it is a prime number
    return True
