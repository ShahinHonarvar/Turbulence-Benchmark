
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Store i in the list of prime numbers
            prime_numbers.append(i)

    # Return the list of all left-truncatable prime numbers less than x, sorted in descending order
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number
def is_prime(n):

    # If the number is not an integer or is less than 2, it is not a prime number
    if not n % 1 == 0 or n < 2:
        return False

    # Check if the number is divisible by any numbers between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number passes all the checks, it is a prime number
    return True
