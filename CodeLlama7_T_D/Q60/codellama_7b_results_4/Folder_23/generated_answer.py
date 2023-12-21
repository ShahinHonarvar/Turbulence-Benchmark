
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through each element in the tuple
    for x in tuple:
        # Check if x is a prime number
        if is_prime(x):
            # If it is, check if it is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(x):
                # If it is, add it to the list of prime numbers
                prime_numbers.append(x)

    # Return the list of prime numbers sorted in descending order
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If i divides n, return False
            if n % i == 0:
                return False

    # If n is a prime number, return True
    return n > 1

# Define a function to check if a number is a left-and-right-truncatable prime number or not
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if is_prime(n):
        # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
        for i in range(len(str(n)))):
            # If the remaining number after removing the leading leftmost digit is not a prime number, return False
            if not is_prime(int(str(n)[1:]))):
                return False

            # If the remaining number after removing the last rightmost digit is not a prime number, return False
            if not is_prime(int(str(n)[:-1]))):
                return False

    # If n is a left-and-right-truncatable prime number, return True
    return True
