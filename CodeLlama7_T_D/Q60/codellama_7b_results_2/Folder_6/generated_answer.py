
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive) and check if each number is a left-and-right-truncatable prime number
    for i in range(1, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If the current number is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # If the number is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of the number, it is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # If the number is less than 10, it cannot be a left-and-right-truncatable prime number
    if n < 10:
        return False

    # Check if the number contains no 0

    if '0' in str(n):
        return False

    # Remove the leading leftmost and last rightmost digits of the number

    leading_leftmost_digit = int(str(n)[1])
    last_rightmost_digit = int(str(n)[:-1])[-1]

    # Check if the removed digits are simultaneously successively removed down to a one- or two-digit prime number

    for i in range(1, leading_leftmost_digit + 1):
        if not is_prime(leading_leftmost_digit - i):
            return False

    for i in range(1, last_rightmost_digit + 1):
        if not is_prime(last_rightmost_digit + i):
            return False

    # If the removed digits are simultaneously successively removed down to a one- or two-digit prime number, the original number is a left-and-right-truncatable prime number
    return True
