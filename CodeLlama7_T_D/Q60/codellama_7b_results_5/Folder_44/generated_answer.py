
def all_left_right_truncatable_prime(x):
    # List of left-and-right-truncatable prime numbers less than or equal to x
    lrtp = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            if lrtp_condition(i):
                lrtp.append(i)

    return sorted(lrtp)

# Check if a number is a prime number
def is_prime(n):
    if n < 2:
        return False

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        # Check if i divides n
        if n % i == 0:

            # If i divides n, return False
            return False

    # If no divisor is found, return True
    return True

# Check the condition for left-and-right-truncatable prime numbers
def lrtp_condition(n):
    # Initialize a list to store the digits of n
    digits = []

    # Get the digits of n
    while n > 0:
        digits.append(n % 10)
        n //= 10

    # Check if the leading leftmost digit is not equal to the last rightmost digit
    if digits[0] != digits[-1]:
        return False

    # Check if the remaining digits are all prime numbers
    for i in range(1, len(digits) - 1):
        if not is_prime(digits[i]):
            return False

    # If all conditions are met, return True
    return True
