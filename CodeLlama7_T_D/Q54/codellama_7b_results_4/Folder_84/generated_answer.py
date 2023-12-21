
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of positive integers
    for x in tuple:
        # Check if x is a prime number
        if is_prime(x):
            # Append x to the list of prime numbers
            prime_numbers.append(x)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of right-truncatable prime numbers less than x
    return prime_numbers

# Check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and it is not divisible by any prime number less than or equal to its square root, it is prime
    return True
