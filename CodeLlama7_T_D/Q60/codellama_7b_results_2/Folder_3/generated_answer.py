
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left- and right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and has no factors other than 1 and itself
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0
    if '0' in str(n):
        # Return False if the number contains any 0
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        # Return False if the number is not a prime number
        return False

    # Check if the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, int(n ** 0.5) + 1)):
        # Check if i divides n
        if n % i == 0:
            # Remove the leading leftmost and last rightmost digits of n by taking the remainder of n divided by i
            remaining_digits = n % (i * i)

            # Check if the remaining digits is a prime number
            if not is_prime(remaining_digits):
                # Return False if the remaining digits is not a prime number
                return False

    # Return True if the number is left-and-right-truncatable prime number
    return True
