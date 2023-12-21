
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x, sorted in ascending order
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and has no prime factor other than itself and 1
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Check if n has no prime factor other than itself and 1
    for i in range(2, int(n ** 0.5) + 1)):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and has no prime factor other than itself and 1
    return True
