
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all the numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all the numbers less than n
        for i in range(2, n):
            # Check if any number divides n without leaving a remainder
            if n % i == 0:
                # Return False if any number divides n without leaving a remainder
                return False

    # Return True if n is greater than 1 and it is not divisible by any number between 2 and n-1
    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains any zero digits
    if "0" in str(n):
        # Return False if the number contains any zero digits
        return False

    # Loop through all the numbers less than n
    for i in range(2, n):
        # Check if any number divides n without leaving a remainder
        if n % i == 0:
            # Check if the remainder is equal to 1
            if (n % i) == 1:
                # Return False if the remainder is not equal to 1
                return False

    # Return True if the number is left-and-right-truncatable prime number
    return True
