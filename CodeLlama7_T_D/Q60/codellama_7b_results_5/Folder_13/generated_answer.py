
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)
    return prime_numbers

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Check if n is a power of 2
    if n & (n - 1) == 0:
        # If n is a power of 2, return False
        return False

    # Check if n has more than one factor
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            # If i divides n, return False
            return False

    # If no factors other than 1 and itself are found, return True
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, return False
        return False

    # Check if the leading leftmost digit of n is equal to 1
    if n % 10 ** (len(str(n))) - len(str(n)) + 1) == 1:
        # If the leading leftmost digit of n is equal to 1, return False
        return False

    # Check if the last rightmost digit of n is equal to 1
    if n % 10 ** (len(str(n))) - len(str(n)) + 1) == 1:
        # If the last rightmost digit of n is equal to 1, return False
        return False

    # If no digits other than 1 and itself are found in the leading leftmost and last rightmost digits of n, return True
    return True
