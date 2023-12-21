 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    right_truncatable_primes = []
    # Iterate through the tuple of integers
    for i in range(len(tuple)):
        # Get the current integer from the tuple
        x = tuple[i]
        # Check if the integer is a prime number
        if is_prime(x):
            # If the integer is a prime number, check if it is a right-truncatable prime number
            if is_right_truncatable_prime(x):
                # If the integer is a right-truncatable prime number, add it to the list of right-truncatable prime numbers
                right_truncatable_primes.append(x)
    # Sort the list of right-truncatable prime numbers in ascending order
    right_truncatable_primes.sort()
    return right_truncatable_primes
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is a prime number, return True
    return True

def is_right_truncatable_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from the last rightmost digit of n to 0
        for i in range(len(str(n))) - 1, -1, -2:
            # Get the current rightmost digit of n
            current_digit = int(str(n)[i]))
            # Check if the current rightmost digit is equal to the previous rightmost digit minus 1
            if current_digit == (int(str(n))[i - 1]) - 1:
                # If the current rightmost digit is equal to the previous rightmost digit minus 1, check if n is still a prime number
                if is_prime(n):
                    # If n is still a prime number, return True
                    return True

    # If n is not a right-truncatable prime number, return False
    return False
