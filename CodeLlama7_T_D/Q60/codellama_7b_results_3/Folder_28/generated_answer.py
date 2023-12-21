
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x, checking if each number is a left-and-right-truncatable prime number
    for i in range(1, x + 1):

        # Check if the current number is a prime number and if it is a left-and-right-truncatable prime number
        if is_prime(i) and is_left_right_truncatable_prime(i):

            # If the current number is a left-and-right-truncatable prime number, add it to the prime list
            prime_list.append(i)

    # Sort the prime list in ascending order and return it
    return sorted(prime_list)

# Define the is_prime function
def is_prime(n):

    # Check if n is equal to 1 or greater than 2
    if n == 1 or n > 2:

        # If n is not equal to 1 and less than or equal to 2, check if it is divisible by any number between 2 and the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # If n is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If n is equal to 1 or greater than 2 and is not divisible by any number between 2 and the square root of n, it is prime
    return True

# Define the is_left_right_truncatable_prime function
def is_left_right_truncatable_prime(n):

    # Check if n contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(1, len(str(n)) - 2):

        # If any digit in the leading leftmost and last rightmost positions is not equal to the previous digit, it is not a left-and-right-truncatable prime number
        if str(n)[i] != str(n)[i - 1]:
            return False

    # If all digits in the leading leftmost and last rightmost positions are simultaneously successively removed down to a one- or two-digit prime number, it is a left-and-right-truncatable prime number
    return True
