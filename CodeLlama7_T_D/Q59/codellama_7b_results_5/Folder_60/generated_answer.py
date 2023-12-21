
def all_left_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of integers
    for integer in tuple_of_integers:
        # Check if the integer is a prime number
        if is_prime(integer):
            # Add the prime number to the list
            prime_numbers.append(integer)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers)

# Define a function to check if an integer is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, n is prime
    return True
