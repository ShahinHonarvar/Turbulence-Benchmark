 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    left_right_truncatable_primes = []
    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Initialize an empty string to store the current number as a string
            num_str = ""

            # Convert the current number to a string and store it in num_str

            # Check if the current number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i, num_str):
                # Add the current number to the list of left-and-right-truncatable prime numbers
                left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes

# Function to check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If yes, return False
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # If yes, return False
        if n % i == 0:
            return False

    # If no factors of n were found, return True
    return True

# Function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n, num_str):
    # Initialize an empty string to store the reversed digits of n as a string
    rev_num_str = ""

    # Convert the reversed digits of n to a string and store it in rev_num_str

    # Check if the number is left-and-right-truncatable prime by removing the leading leftmost and last rightmost digits simultaneously successively

        # If yes, return True
        return True

    # If no factors of n were found, return False
    return False
