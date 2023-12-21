
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and n - 1, it is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the number contains any 0 digit
    if '0' in str(n):
        return False

    # Check if the number is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it does not contain any 0 digit and it is not divisible by any number between 2 and n - 1, it is left-and-right-truncatable prime number
    return True
