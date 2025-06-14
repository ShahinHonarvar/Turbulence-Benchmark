
def all_left_truncatable_prime(tuple_of_primes):
    # Initialize an empty list to store the left-truncatable prime numbers
    left_truncatable_primes = []
    # Iterate over the tuple of prime numbers
    for prime in tuple_of_primes:
        # Check if the current prime number is a left-truncatable prime number
        if is_left_truncatable_prime(prime):
            # Add the current prime number to the list of left-truncatable prime numbers
            left_truncatable_primes.append(prime)
    # Return the sorted list of left-truncatable prime numbers
    return sorted(left_truncatable_primes)
# Define a function to check if a given number is a left-truncatable prime number
def is_left_truncatable_prime(n):
    # Check if the current number is a prime number
    if not is_prime(n):
        return False

# Check if the leading leftmost digit of the current number is successively removed, then all resulting numbers are prime
for i in range(1, len(str(n)))):
    num = int(str(n)[:i])
    if not is_prime(num):
        return False

# If all checks pass, then the current number is a left-truncatable prime number
return True

# Define a function to check if a given number is a prime number
def is_prime(n):
    # Check if the current number is less than 2
    if n < 2:
        return False

# Check if the current number has any factors other than 1 and itself
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        return False
