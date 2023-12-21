
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
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is 1 or less
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and sqrt(n) (inclusive)
    for i in range(2, int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False

    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n contains any 0 digit
    if '0' in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(1, len(str(n))) + 1):
        if is_prime(int(str(n)[0:i] + str(n)[i+1:])))):
            return True

    return False
