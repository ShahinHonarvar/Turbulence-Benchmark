
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all integers from 1 to x
    for i in range(1, x + 1):

        # Check if the current integer is a prime number
        if is_prime(i):

            # Check if the current integer is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the current integer to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_list, reverse=True)

def is_left_right_truncatable_prime(n):
    # Initialize a variable to store the current number
    current = n

    # Loop through all digits of the current number from left to right
    for digit in str(current):

        # Check if the current digit is 0
        if digit == '0':

            # Return False if any digit is 0
            return False

    # Initialize a variable to store the leading digits of the current number
    leading = ''

    # Initialize a variable to store the trailing digits of the current number
    trailing = ''

    # Get the leading and trailing digits of the current number
    for digit in str(current):

        if digit != '0':

            leading += digit


    for digit in reversed(str(current)):

        if digit != '0':

            trailing += digit


    # Check if the leading and trailing digits of the current number are equal
    if leading == trailing:

        # Return True if the leading and trailing digits of the current number are equal
        return True

    else:

        # Return False if the leading and trailing digits of the current number are not equal
        return False

def is_prime(n):

    # Check if n is an integer greater than 1
    if n > 1:

        # Initialize a variable to store the smallest factor of n
        factor = 2

        # Loop through all odd numbers greater than 1
        while factor * factor <= n:

            # Check if the current factor divides n
            if n % factor == 0:

                # Return False if any odd number greater than 1 divides n
                return False

            # Increment the current factor by 1
            factor += 1

    # If n is a perfect square
    if math.sqrt(n) == int(math.sqrt(n)):

        # Return True if n is a perfect square
        return True

    else:

        # Return False if n is not a perfect square
        return False
