
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the list of left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # If the number is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if the number is divisible by any other number apart from itself and 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is greater than 1, it is a prime number
    return True

# Check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):

    # If the number is less than 2, it is not a left-and-right-truncatable prime number
    if n < 2:
        return False

    # Check if the number is divisible by any other number apart from itself and 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number contains a zero, it is not a left-and-right-truncatable prime number
    if "0" in str(n):
        return False

    # If the number is greater than 1, it is a left-and-right-truncatable prime number
    return True
