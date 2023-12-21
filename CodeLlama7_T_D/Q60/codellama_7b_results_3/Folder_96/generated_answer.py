
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all integers from 1 to x
    for i in range(1, x + 1):
        # Check if the current integer is a prime number
        if is_prime(i):
            # Check if the current integer is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current integer to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if an integer is a prime number
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

    # If the loop completes successfully, return True
    return True

# Define a function to check if an integer is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    # This condition is implemented by checking if the resulting number is a prime number.
    for i in range(2, len(str(n)))):
        for j in range(i + 1, len(str(n)) - 1):
            if is_prime(int(str(n)[0:j] + str(n)[j + 1:])))
                return True

    # If the loop completes successfully, return False
    return False
