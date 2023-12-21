
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for i in range(len(tuple)):
        # Get the current number from the tuple
        current_number = tuple[i]

        # Check if the current number is a prime number
        if is_prime(current_number):
            # If the current number is a prime number, add it to the list of prime numbers
            prime_numbers.append(current_number)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        # If n is less than 2, it is not prime
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        # If n is divisible by i, it is not prime
        if n % i == 0:
            return False

    # If n is greater than 1 and it is not divisible by 2 to n-1, it is prime
    return True
