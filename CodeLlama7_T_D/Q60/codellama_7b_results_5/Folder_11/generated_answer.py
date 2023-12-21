
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x, inclusive
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of prime numbers sorted in ascending order
    return sorted(prime_numbers)

# Check if a number is prime using the Sieve of Eratosthenes algorithm
def is_prime(n):
    # If n is less than 2, it is not prime
    if n < 2:
        return False

    # Mark all numbers up to and including the square root of n as composite
    sieve = [True] * (n + 1)
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    # Return True if n is prime and False otherwise
    return sieve[n]

# Check if a number is left-and-right-truncatable prime number using the definition given in the problem statement
def is_left_right_truncatable_prime(n):
    # If n is less than 2, it is not prime
    if n < 2:
        return False

    # Check if n contains any zeros
    if "0" in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(len(str(n)) - 1, -1, -1):
        num = int(str(n)[:i] + str(n)[i+1:]))
        if is_prime(num):
            return True

    # If no left-and-right-truncatable prime number exists in the specified range, return False
    return False
