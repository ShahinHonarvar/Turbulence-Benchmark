
def all_right_truncatable_prime(n):
    # Initialize an empty list for the prime numbers
    prime_numbers = []

    # Loop through all numbers less than n
    for i in range(2, n):
        # Check if i is a prime number using the primality function
        if is_prime(i):
            # Check if i is a right-truncatable prime number using the truncatability function
            if is_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers = sorted(prime_numbers)

    return prime_numbers

# Define a function for checking primality
def is_prime(n):
    # Check if n is an integer
    if not isinstance(n, int):
        raise ValueError("n must be an integer")

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Define a function for checking truncatability
def is_right_truncatable_prime(n):
    # Check if n is an integer
    if not isinstance(n, int):
        raise ValueError("n must be an integer")

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if the last rightmost digit of n is prime
    if not is_prime(int(str(n)[-1]))):
        return False

    # Check if the number obtained by removing the last rightmost digit from n is prime
    if not is_prime(n % int(str(n)[-1])))):
        return False

    return True
