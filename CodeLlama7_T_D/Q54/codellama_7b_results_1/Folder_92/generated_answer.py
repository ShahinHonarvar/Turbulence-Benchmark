
def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 2 to n - 1
    for i in range(2, n - 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is right-truncatable
            if is_right_truncatable(i):

                # Add i to the list of primes
                primes.append(i)

    # Sort the list of primes in ascending order
    primes = sorted(primes)

    # Return the list of primes
    return primes

# Check if a number is prime
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:

        # Return False
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):

        # Check if i divides n
        if n % i == 0:

            # Return False
            return False

    # Return True
    return True

# Check if a number is right-truncatable
def is_right_truncatable(n):

    # Initialize an empty list to store the digits of n
    digits = []

    # Get the digits of n in reverse order
    while n > 0:

        # Add the last digit of n to the list of digits
        digits.append(n % 10)

        # Remove the last digit of n
        n //= 10

    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 2 to n - 1
    for i in range(2, n - 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is right-truncatable
            if is_right_truncatable(i):

                # Add i to the list of primes
                primes.append(i)

    # Sort the list of primes in ascending order
    primes = sorted(primes)

    # Return the list of primes
    return primes
