
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the range of numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # Check if the current number is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if the number is greater than 1
    if n > 1:

        # Loop through the range of numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if the current number is divisible by the loop variable
            if n % i == 0:

                # Return False since the number is not a prime number
                return False

    # Return True since the number is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Initialize variables to store the leading and last digits of the current number
    leading_digit = -1
    last_digit = -1

    # Loop through the digits of the current number
    for digit in str(n):

        # Check if the current digit is the leading digit
        if leading_digit == -1:

            # Set the leading digit to the current digit
            leading_digit = int(digit)

        # Check if the current digit is the last digit
        if last_digit == -1:

            # Set the last digit to the current digit
            last_digit = int(digit)

    # Check if the leading and last digits are not equal to each other
    if leading_digit != last_digit:

        # Return False since the leading and last digits are not equal to each other
        return False

    # Check if the leading and last digits are both greater than 0
    if leading_digit <= 0 or last_digit <= 0:

        # Return False since the leading and last digits are both less than or equal to 0
        return False

    # Initialize a variable to store the number of times the leading digit is removed from the current number
    leading_digit_removal = 0

    # Initialize a variable to store the number of times the last digit is removed from the current number
    last_digit_removal = 0

    # Loop through the range of numbers from the square root of n down to 1
    for i in range(int(n ** 0.5), 1, -1):

        # Check if the current number is a prime number
        if is_prime(n // i):

            # Increment the number of times the leading digit is removed from the current number
            leading_digit_removal += 1

            # Increment the number of times the last digit is removed from the current number
            last_digit_removal += 1

            # Check if the number of times the leading digit is removed from the current number equals the number of times the last digit is removed from the current number
            if leading_digit_removal == last_digit_removal:

                # Return True since the current number is a left-and-right-truncatable prime number
                return True

    # Return False since the current number is not a left-and-right-truncatable prime number
    return False
