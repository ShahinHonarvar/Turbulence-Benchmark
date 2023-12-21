
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

def is_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # Check if n is a multiple of 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If n is a prime number, return True
    return True

def is_left_right_truncatable_prime(n):
    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the leading leftmost digit of n is a prime number
    if not is_prime(int(str(n)[1:])):
        return False

    # Check if the last rightmost digit of n is a prime number
    if not is_prime(int(str(n)[:-1]))):
        return False

    # If n is a left-and-right-truncatable prime number, return True
    return True
