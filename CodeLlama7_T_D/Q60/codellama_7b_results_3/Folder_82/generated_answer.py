
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left- and right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if n is divisible by i
            if n % i == 0:
                # Return False if n is divisible by i
                return False

    # Return True if n is greater than 1 and not divisible by any number between 2 and the square root of n
    return True

def is_left_right_truncatable_prime(n):
    # Check if n contains 0
    if '0' in str(n):
        # Return False if n contains 0
        return False

    # Iterate from the leftmost digit to the rightmost digit
    for i in range(len(str(n)))):
        # Check if removing the leading leftmost digit of n results in a prime number
        if is_prime(int(str(n)[1:]))) and (i == 0):
            # Check if removing the last rightmost digit of n results in a prime number
            if is_prime(int(str(n)[:-1]))) and (i == len(str(n)))):
                # Return True if n is left-and-right-truncatable prime number
                return True

    # Return False if n is not a left-and-right-truncatable prime number
    return False
