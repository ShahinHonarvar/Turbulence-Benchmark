
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the range of values from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # Return False if n is less than or equal to 1
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # Check if n is divisible by i
        if n % i == 0:
            # Return False if n is divisible by i
            return False

    # Return True if n is a prime number
    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the current number contains 0
    if "0" in str(n):
        # Return False if the current number contains 0
        return False

    # Check if the current number is a prime number
    if not is_prime(n):
        # Return False if the current number is not a prime number
        return False

    # Create a list of all digits in the current number
    digits = [int(digit) for digit in str(n)]

    # Check if the first digit is equal to 1
    if digits[0] == 1:
        # Return False if the first digit is equal to 1
        return False

    # Check if the last digit is equal to 1
    if digits[-1] == 1:
        # Return False if the last digit is equal to 1
        return False

    # Create a list of all left-truncatable prime numbers less than or equal to x
    left_truncatable_prime_numbers = []

    # Loop through the range of values from 1 to x
    for i in range(1, x + 1):
        # Check if the current number is a left-truncatable prime number
        if is_left_truncatable_prime(i):
            # Add the current number to the list of left-truncatable prime numbers less than or equal to x
            left_truncatable_prime_numbers.append(i)

    # Check if the first digit of the current number is equal to any of the digits in the list of left-truncatable prime numbers less than or equal to x
    for i in range(len(left_truncatable_prime_numbers)):
        # Check if the first digit of the current number is equal to any of the digits in the list of left-truncatable prime numbers less than or equal to x
        if digits[0] == left_truncatable_prime_numbers[i]:
            # Return False if the first digit of the current number is equal to any of the digits in the list of left-truncatable prime numbers less than or equal to x
            return False

    # Create a list of all right-truncatable prime numbers less than or equal to x
    right_truncatable_prime_numbers = []

    # Loop through the range of values from 1 to x
    for i in range(1, x + 1):
        # Check if the current number is a right-truncatable prime number
        if is_right_truncatable_prime(i):
            # Add the current number to the list of right-truncatable prime numbers less than or equal to x
            right_truncatable_prime_numbers.append(i)

    # Check if the last digit of the current number is equal to any of the digits in the list of right-truncatable prime numbers less than or equal to x
    for i in range(len(right_truncatable_prime_numbers)):
        # Check if the last digit of the current number is equal to any of the digits in the list of right-truncatable prime numbers less than or equal to x
        if digits[-1] == right_truncatable_prime_numbers[i]:
            # Return False if the last digit of the current number is equal to any of the digits in the list of right-truncatable prime numbers less than or equal to x
            return False

    # Return True if the first digit of the current number is not equal to 1, and if the last digit of the current number is not equal to 1, and if the current number does not contain any 0s
    return True
# Function to find the right-and-left-truncatable prime numbers less than or equal to x
def find_right_left_truncatable_prime_numbers(x):
    # Create a list of all right-and-left-truncatable prime numbers less than or equal to x
    right_left_truncatable_prime_numbers = []

    # Loop through the range of values from 1 to x
    for i in range(1, x + 1):
        # Check if the current number is a right-and-left-truncatable prime number
        if is_right_left_truncatable_prime(i):
            # Add the current number to the list of right-and-left-truncatable prime numbers less than or equal to x
            right_left_truncatable_prime_numbers.append(i)

    # Return the list of right-and-left-truncatable prime numbers less than or equal to x
    return right_left_truncatable_prime_numbers
# Function to find the sum of all the right-and-left-truncatable prime numbers less than or equal to x
def find_sum_right_left_truncatable_prime_numbers(x):
    # Create a list of all right-and-left-truncatable prime numbers less than or equal to x
    right_left_truncatable_prime_numbers = find_right_left_truncatable_prime_numbers(x)

    # Return the sum of all the right-and-left-truncatable prime numbers less than or equal to x
    return sum(right_left_truncatable_prime_numbers)
# Function to find the right-truncatable number with a given set of digits
def is_right_truncatable_number(x):
    # Check if the current number contains any 0s
    for digit in str(x):
        # Return False if the current number contains any 0s
        if digit == "0":
            return False

    # Check if the first digit of the current number is equal to 1
    if x[0] == "1":
        # Return False if the first digit of the current number is equal to 1
        return False

    # Loop through the range of values from 2 to the square root of the maximum value of the current number
    for i in range(2, int(math.sqrt(x)))):
        # Check if the current number is divisible by any number greater than 1 and less than or equal to the square root of the maximum value of the current number
        if x % i == 0:
            # Return False if the current number is divisible by any number greater than 1 and less than or equal to the square root of the maximum value of the current number
            return False

    # Return True if the first digit of the current number is not equal to 1, and if the last digit of the current number is not equal to 1, and if the current number does not contain any 0s
    return True
# Function to find the right-truncatable number with a given set of digits
def is_left_truncatable_number(x):
    # Check if the last digit of the current number is equal to 1
    if x[-1] == "1":
        # Return False if the last digit of the current number is equal to 1
        return False

    # Loop through the range of values from 2 to the square root of the maximum value of the current number
    for i in range(2, int(math.sqrt(x)))):
        # Check if the current number is divisible by any number greater than 1 and less than or equal to the square root of the maximum value of the current number
        if x % i == 0:
            # Return False if the current number is divisible by any number greater than 1 and less than or equal to the square root of the maximum value of the current number
            return False

    # Return True if the last digit of the current number is not equal to 1, and if the current number does not contain any 0s
    return True
# Function to find the right-and-left-truncatable number with a given set of digits
def is_right_left_truncatable_number(x):
    # Return False if the current number contains any 0s
    for digit in str(x):
        # Return False if the current number contains any 0s
        if digit == "0":
            return False

    # Check if the first digit of the current number is equal to 1
    if x[0] == "1":
        # Return False if the first digit of the current number is equal to 1
        return False

    # Check if the last digit of the current number is equal to 1
    if x[-1] == "1":
        # Return False if the last digit of the current number is equal to 1
        return False

    # Loop through the range of values from 2 to the square root of the maximum value of the current number
    for i in range(2, int(math.sqrt(x)))):
        # Check if the current number is divisible by any number greater than 1 and less than or equal to the square root of the maximum value of the current number
        if x % i == 0:
            # Return False if the current number is divisible by any number greater than 1 and less than or equal to the square root of the maximum value of the current number
            return False

    # Return True if the first digit of the current number is not equal to 1, and if the last digit of the current number is not equal to 1, and if the current number does not contain any 0s
    return True
# Function to check if a given set of digits contains a palindrome
def is_palindromic_number(x):
    # Return False if the length of the given set of digits is less than or equal to 1
    if len(str(x)) <= 1:
        # Return False if the length of the given set of digits is less than or equal to 1
        return False

    # Loop through the range of values from the second digit of the current number to the last digit of the current number in reverse order
    for i in range(len(str(x)))-2, len(str(x)))-1:
        # Check if the current digit is equal to the previous digit
        if str(x)[i] == str(x)[i-1]:
            # Return True if the length of the given set of digits is greater than 1 and the current digit is equal to the previous digit
            return True

    # Return False if the length of the given set of digits is greater than 1 and the current digit is not equal to the previous digit
    return False
# Function to find the first 8 truncatable primes below one-thousand
def main():
    sum = 0
    # Loop through the range of values from 2 to 999
    for i in range(2, 1000):
        # Check if the current number is a prime number
        if is_prime(i) == True:
            # Check if the current number is truncatable
            if is_truncatable_number(i) == True:
                # Add the sum of the current number to the total sum
                sum += i

    # Return the total sum of the first 8 truncatable primes below one-thousand
    return sum
