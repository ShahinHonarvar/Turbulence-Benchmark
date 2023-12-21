
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate through all prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in ascending order
    prime_list = sorted(prime_list)

    # Return the list of prime numbers
    return prime_list

# Function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to n - 1
        for i in range(2, n):

            # If i divides n, return False
            if n % i == 0:
                return False

    # If n is a prime number, return True
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Initialize an empty string to store the leading leftmost and last rightmost digits of n
    leading_leftmost = ''
    last_rightmost = ''

    # Get the length of n in digits
    n_length = len(str(n))

    # Iterate from 1 to n - 1
    for i in range(1, n_length):

        # If the digit at position i is not equal to the last rightmost digit, return False
        if str(n)[i] != last_rightmost:
            return False

        # If the digit at position i is not equal to the leading leftmost digit, return False
        if str(n)[i] != leading_leftmost:
            return False

    # Return True if n is a left-and-right-truncatable prime number
    return True
