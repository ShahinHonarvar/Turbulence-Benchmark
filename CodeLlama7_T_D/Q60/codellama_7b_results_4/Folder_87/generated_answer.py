
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list, reverse=True)

# Function to check if a number is prime
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all numbers from 2 to n - 1
        for i in range(2, n):

            # If the remainder of n / i is 0, then return False
            if n % i == 0:
                return False

    # Return True if the number is prime
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n contains 0
    if '0' in str(n):
        return False

    # Loop through all numbers from 2 to n - 1
    for i in range(2, n):

        # If the remainder of n / i is 0, then return False
        if n % i == 0:
            return False

    # Return True if the number is left-and-right-truncatable prime number
    return True
