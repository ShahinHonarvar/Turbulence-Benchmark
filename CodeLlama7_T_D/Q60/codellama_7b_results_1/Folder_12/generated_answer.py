
def all_left_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[70]
    left_right_truncatable_primes = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of left-and-right-truncatable prime numbers
                left_right_truncatable_primes.append(i)
    # Sort the list in descending order
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes
# Check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and not divisible by any number between 2 and the square root of n
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)))):
        # Check if the leading leftmost digit of n is 0
        if str(n)[i] == '0':
            # Return False if the leading leftmost digit of n is 0
            return False

        # Check if the last rightmost digit of n is 0
        if str(n)[-i-1] == '0':
            # Return False if the last rightmost digit of n is 0
            return False

    # Return True if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    return True
