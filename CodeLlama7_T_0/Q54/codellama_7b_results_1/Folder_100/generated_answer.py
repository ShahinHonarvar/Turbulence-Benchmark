
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple of positive integers
    for i in range(len(tuple)):
        # Get the current number from the tuple
        current_number = tuple[i]

        # Check if the current number is a prime number
        if is_prime(current_number):
            # If the current number is a prime number, add it to the list of prime numbers
            prime_numbers.append(current_number)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is a prime number
    return True
