
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the numbers from 1 to x
    for num in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(num):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):
                # Add the prime number to the list of prime numbers
                prime_numbers.append(num)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

def is_prime(num):
    # Check if the number is greater than 1
    if num > 1:
        # Loop through the numbers from 2 to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if num % i == 0:
                # Return False if the number is divisible by any number between 2 and the square root of the number
                return False

    # Return True if the number is greater than 1 and not divisible by any number between 2 and the square root of the number
    return True

def is_left_right_truncatable_prime(num):
    # Check if the number contains no 0
    if '0' in str(num):
        # Return False if the number contains a 0
        return False

    # Loop through the numbers from 1 to the square root of the number
    for i in range(1, int(num ** 0.5) + 1):
        # Check if the number is divisible by any number between 1 and the square root of the number
        if num % i == 0:
            # Return False if the number is divisible by any number between 1 and the square root of the number
            return False

    # Loop through the numbers from the last rightmost digit to the first leftmost digit of the number
    for i in range(len(str(num)))-1, -1, -1:
        # Check if the number is divisible by any number between the last rightmost digit and the first leftmost digit of the number
        if num % int(str(num)[i:])) == 0:
            # Return False if the number is divisible by any number between the last rightmost digit and the first leftmost digit of the number
            return False

    # If the number passes all checks, it is a left-and-right-truncatable prime number
    return True
