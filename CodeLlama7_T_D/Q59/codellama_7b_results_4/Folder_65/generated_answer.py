
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers less than x
    for i in range(2, x):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-truncatable prime number
            if is_left_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

        # If the number is not divisible by 2 to n-1, it is prime
        return True

# Define a function to check if a number is left-truncatable prime number
def is_left_truncatable_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if the leading digit of n is not equal to 0
        if str(n)[0] != '0':

            # Remove the leading leftmost digit of n and check if the resulting number is prime
            if is_prime(int(str(n))[1:])):
                return True

    # If the number is not a prime or it does not satisfy the condition, it is not a left-truncatable prime number
    return False
