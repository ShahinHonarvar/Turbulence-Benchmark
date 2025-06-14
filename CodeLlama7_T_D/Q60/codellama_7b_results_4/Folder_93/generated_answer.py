
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Check if n is an odd number
    if n % 2 == 0:
        return False

    # Check if n has any prime factors other than 2 and 3
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If n is a prime number, return True
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost digit of n is a 1 or a 2
    if n // 10 ** (len(str(n))) - 1) % 10 != 1 and n // 10 ** (len(str(n))) - 1) % 10 != 2:
        return False

    # Check if the last rightmost digit of n is a 1 or a 3
    if n % 10 == 1 or n % 10 == 3:
        return False

    # If all checks pass, return True
    return True
