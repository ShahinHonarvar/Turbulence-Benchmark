
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (both inclusive) and check if each number is a left-and-right-truncatable prime number
    for num in range(1, x + 1):

        # Check if the number is divisible by any other number between 1 and sqrt(num) (both inclusive)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break

        # If the number is not divisible by any other number between 1 and sqrt(num) (both inclusive), it is a prime number
        else:

            # Check if the number is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # If the number is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(num)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(num):

    # Check if the number is divisible by any other number between 1 and sqrt(num) (both inclusive)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break

    # If the number is not divisible by any other number between 1 and sqrt(num) (both inclusive), it is a prime number
    else:

        # Check if the number contains no 0s
        if '0' not in str(num):

            # Initialize an empty list to store the digits of the number
            digits = []

            # Extract the digits of the number and store them in the list
            for digit in str(num):
                digits.append(int(digit))

            # Check if all the digits of the number are not equal to each other
            if len(digits) == len(set(digits)):

                # Initialize an empty string to store the digits of the number, starting from the last digit and ending with the first digit
                num_string = ''

                # Extract the digits of the number in reverse order (from the last digit to the first digit) and concatenate them into a single string
                for digit in reversed(digits):
                    num_string += str(digit)

                # Convert the string back into an integer
                num = int(num_string)

                # Check if the number is still prime after being truncated from both left and right sides
                if is_prime(num):

                    # If the number is still prime, return True to indicate that it is a left-and-right-truncatable prime number
                    return True

        # If the number contains 0s, return False to indicate that it is not a left-and-right-truncatable prime number
        else:
            return False

# Function to check if a number is a prime number
def is_prime(num):

    # Check if the number is less than or equal to 1
    if num <= 1:

        # If the number is less than or equal to 1, it is not a prime number
        return False

    # Check if the number is divisible by any other number between 1 and sqrt(num) (both inclusive)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break

    # If the number is not divisible by any other number between 1 and sqrt(num) (both inclusive), it is a prime number
    else:
        return True

# Function to test whether or not a given number is a left-and-right-truncatable prime number
def test_left_right_truncatable_prime(num):

    # Check if the number is less than 10
    if num < 10:
        return False

    # Check if the number is a left-and-right-truncatable prime number
    else:
        return is_left_right_truncatable_prime(num)
