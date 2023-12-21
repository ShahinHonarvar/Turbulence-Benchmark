 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        # Check if the number is a prime number and also satisfies the left-and-right-truncatable prime condition
        if isprime(i) and i == lrtrp(i, 0)):
            # Add the left-and-right-truncatable prime number to the list
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)
# Define a function to check if a number is a prime number
def isprime(n):
    # Check if n is an integer greater than 1
    if not (n > 1 and n % 2 != 0):
        return False

    # Check if n is divisible by any number between 3 and the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    # If the above loop does not return False, then n is a prime number
    return True

# Define a function to check if a number is left-and-right-truncatable prime or not
def lrtrp(n, d):
    # Initialize a variable to store the result of the modulo operation
    m = 0

    # Check if the number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the number is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    # If the above loop does not return False, then n is a prime number
    return True
