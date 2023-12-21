
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple of positive integers
    for i in range(49):
        # Get the integer at index i
        x = tuple[i]

        # Check if x is a prime number
        if is_prime(x):
            # If x is a prime number, add it to the list of prime numbers
            prime_numbers.append(x)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of right-truncatable prime numbers less than x
    return prime_numbers

# Check if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the numbers between 2 and the square root of the number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        # If n is divisible by any number between 2 and the square root of n, it is not prime
        if n % i == 0:
            return False

    # If n is not divisible by any number between 2 and the square root of n, it is prime
    return True
