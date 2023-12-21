
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is greater than 1
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # Return False if n is not a prime number
        return False

    # Initialize an empty list to store the digits of n
    digits = []

    # Get the digits of n
    for digit in str(n):

        # Add the digit to the list of digits
        digits.append(int(digit))

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(len(digits) - 1, 0, -1):

        # Remove the ith digit from n
        n = int(str(n)[:i] + str(n)[i + 1:]))

        # Check if n is a prime number
        if not is_prime(n):

            # Return False if n is not a prime number
            return False

    # Return True if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number
    return True
