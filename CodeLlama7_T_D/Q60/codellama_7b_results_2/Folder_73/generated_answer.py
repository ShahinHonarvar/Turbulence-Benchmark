
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_list.append(i)

    # Sort the list in ascending order
    prime_list.sort()

    # Return the list of prime numbers
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is greater than 1, it is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # If the number is not a prime number, it is not left-and-right-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number is left-truncatable prime number
    if not is_left_truncatable_prime(n):
        return False

    # Check if the number is right-truncatable prime number
    if not is_right_truncatable_prime(n):
        return False

    # If the number is left-and-right-truncatable prime number, it is prime
    return True

# Check if a number is left-truncatable prime number
def is_left_truncatable_prime(n):
    # If the number is not a prime number, it is not left-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is greater than 1, it is left-truncatable prime number
    return True

# Check if a number is right-truncatable prime number
def is_right_truncatable_prime(n):
    # If the number is not a prime number, it is not right-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is greater than 1, it is right-truncatable prime number
    return True
