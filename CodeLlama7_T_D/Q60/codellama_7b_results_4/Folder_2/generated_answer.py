
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x, inclusive
    for num in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(num):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):
                # Add the number to the list of prime numbers
                prime_numbers.append(num)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):
    # If the number is less than 2, it is not a prime number
    if n < 2:
        return False

    # If the number is divisible by any number between 2 and the square root of the number, it is not a prime number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number makes it all the way to here, it is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # If the number is not a prime number, it is not a left-and-right-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number can be truncatable by removing leading and last digits
    if not is_left_truncatable_prime(n) or not is_right_truncatable_prime(n):
        return False

    # If the number makes it all the way to here, it is a left-and-right-truncatable prime number
    return True

# Check if a number is a left-truncatable prime number
def is_left_truncatable_prime(n):
    # If the number is not a prime number, it is not a left-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number can be truncatable by removing leading digits
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_left_truncatable_prime(i):
            return True

    # If the number makes it all the way to here, it is not a left-truncatable prime number
    return False

# Check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # If the number is not a prime number, it is not a right-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number can be truncatable by removing last digits
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_right_truncatable_prime(i):
            return True

    # If the number makes it all the way to here, it is not a right-truncatable prime number
    return False
