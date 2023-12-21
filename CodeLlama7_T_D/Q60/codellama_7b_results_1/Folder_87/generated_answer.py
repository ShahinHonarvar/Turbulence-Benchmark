
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than or equal to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        # Return False if n is not a positive integer
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        # If n is divisible by i, it is not prime
        if n % i == 0:
            # Return False if n is divisible by i
            return False

    # Return True if n is a prime number
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        # Return False if n is not a positive integer
        return False

    # Check if the leading leftmost digit of n is equal to its last rightmost digit
    if str(n)[0] != str(n)[-1]:
        # If the leading leftmost digit of n is not equal to its last rightmost digit, it is not a left-and-right-truncatable prime number
        return False

    # Check if the string representation of n without its leading leftmost digit and its last rightmost digit is a valid integer
    try:
        # Convert the string representation of n without its leading leftmost digit and its last rightmost digit to an integer
        int(str(n)[1:-1]))
    except ValueError:
        # If the string representation of n without its leading leftmost digit and its last rightmost digit is not a valid integer, it is not a left-and-right-truncatable prime number
        return False

    # Return True if n is a left-and-right-truncatable prime number
    return True
