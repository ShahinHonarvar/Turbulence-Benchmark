
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for i in range(len(tuple)):
        # Set the current integer as x
        x = tuple[i]

        # Check if x is a prime number
        if is_prime(x):
            # If x is a prime number, add it to the list of prime numbers
            prime_numbers.append(x)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers, reverse=True)

# Check if a number is prime by iterating from 2 to the square root of the number
def is_prime(n):
    # Base case: if n is less than or equal to 1, it is not prime
    if n <= 1:
        return False

    # Loop through all integers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If any integer divides n without leaving a remainder, it is not prime
        if n % i == 0:
            return False

    # If no integers divide n without leaving a remainder, it is prime
    return True
