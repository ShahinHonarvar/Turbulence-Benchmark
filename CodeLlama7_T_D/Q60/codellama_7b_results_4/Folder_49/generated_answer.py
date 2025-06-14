
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_list.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_list)

# Check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n
            if n % i == 0:

                # Return False if i divides n
                return False

    # If the loop completes successfully, return True
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Initialize variables to store the leading leftmost and last rightmost digits of n
    leading_digit = 0
    leftmost_digit = 0
    rightmost_digit = 0

    # Loop through all numbers from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1):

        # Check if i divides n
        if n % i == 0:

            # Extract the leading leftmost and last rightmost digits of n/i
            leading_digit = str(n // i)[0]
            leftmost_digit = str(n // i)[1:]
            rightmost_digit = str(n // i)[::-1][1:]

            # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number
            if is_prime(int(leading_digit)) and is_prime(int(leftmost_digit)) and is_prime(int(rightmost_digit))):

                # Return True if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number
                return True

    # If the loop completes successfully, return False
    return False
