
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the range of numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if the number is greater than 1
    if n > 1:

        # Iterate through the range of numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # Check if the number is divisible by any number between 2 and the square root of n
            if n % i == 0:

                # Return False if the number is not a prime number
                return False

    # Return True if the number is a prime number
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number is a prime number
    if not is_prime(n):

        # Return False if the number is not a prime number
        return False

    # Initialize an empty list to store the digits of the number
    digits = []

    # Iterate through the range of numbers from 1 to the number of digits in n
    for i in range(1, len(str(n)) + 1):

        # Append the current digit of the number to the list of digits
        digits.append(int(str(n)[i - 1])))

    # Check if the leading leftmost digit of the number is equal to 1
    if digits[0] == 1:

        # Return False if the leading leftmost digit of the number is not equal to 1
        return False

    # Check if the last rightmost digit of the number is equal to 1
    if digits[-1] == 1:

        # Return False if the last rightmost digit of the number is not equal to 1
        return False

    # Initialize an empty list to store the remaining digits of the number
    remaining_digits = []

    # Iterate through the range of numbers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1)):

        # Check if the current digit is not equal to any of the remaining digits
        if digits[i] != remaining_digits:

            # Append the current digit to the list of remaining digits
            remaining_digits.append(digits[i])

    # Return False if there are any duplicates in the list of remaining digits
    if len(remaining_digits) < len(set(remaining_digits)):

        # Return False if there are any duplicates in the list of remaining digits
        return False

    # Return True if all the conditions are met
    return True
