
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

                # Append the digits of i to the string digits
                digits += j

            # Check if the leading leftmost and last rightmost digits of i are simultaneously successively removed down to a one- or two-digit prime number
            if is_prime(digits[:-1]) and is_prime(digits[1:]):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all integers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and has no factors other than 1 and itself
    return True
