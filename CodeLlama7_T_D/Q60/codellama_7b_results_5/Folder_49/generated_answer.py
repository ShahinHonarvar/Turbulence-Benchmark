 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []
    # Iterate from 2 to x, inclusive
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                result.append(i)
    return sorted(result)

def is_prime(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # Check if n is equal to 1 or 2
    if n in [1, 2]:
        return False
    # Check if n is divisible by any number between 3 and the square root of n
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

def is_left_right_truncatable_prime(n):
    # Check if n contains the digit 0
    if '0' in str(n):
        return False
