
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Initialize an empty string to store the digits of i
            digits = ""

            # Loop through all the digits of i
            for j in str(i):

                # Append each digit of i to digits
                digits += j

            # Check if digits is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(digits):

                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_numbers)

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        # Return False if n is not a prime number
        return False

    # Initialize an empty string to store the digits of n
    digits = ""

    # Loop through all the digits of n
    for i in str(n):

        # Append each digit of n to digits
        digits += i

    # Check if removing the leading leftmost and last rightmost digits from digits results in a one- or two-digit prime number
    return is_prime(int(digits[1:])) or is_prime(int(digits[:-1]))

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the integers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # If n is divisible by i, it is not a prime number
            if n % i == 0:

                # Return False if n is divisible by i
                return False

    # If n is greater than 1 and is not divisible by any integer from 2 to the square root of n, it is a prime number
    return True
