
def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[96]
    prime_numbers = []

    # Loop through the range of numbers less than x
    for i in range(2, x):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is right-truncatable prime number
            if is_right_truncatable_prime(i):
                # Add the number to the list of right-truncatable prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of n, it is a prime number
    return True

# Define a function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the last digit of n is equal to 1
    if int(str(n)[-1]) != 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of n, it is a right-truncatable prime number
    return True
