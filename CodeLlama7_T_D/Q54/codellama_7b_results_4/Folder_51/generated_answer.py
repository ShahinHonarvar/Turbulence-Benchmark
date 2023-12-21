
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple of integers
    for i in range(len(tuple)):
        # Get the current integer from the tuple
        current_integer = tuple[i]

        # Check if the current integer is a prime number
        if is_prime(current_integer):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(current_integer)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by any number between 2 and n-1, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n-1, it is prime
    return True
