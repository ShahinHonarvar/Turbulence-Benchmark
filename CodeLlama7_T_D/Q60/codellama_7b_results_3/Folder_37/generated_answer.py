
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate through all numbers less than or equal to x
    for num in range(2, x + 1):
        # Check if num is a prime number
        if is_prime(num):
            # Check if num is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):
                # Add num to the list of prime numbers
                prime_list.append(num)
    return sorted(prime_list, reverse=True)

def is_prime(num):
    # Check if num is a multiple of 2
    if num % 2 == 0:
        return False

    # Check if num is a multiple of 3
    if num % 3 == 0:
        return False

    # Check if num is a multiple of 5
    if num % 5 == 0:
        return False

    # Check if num is a multiple of 7
    if num % 7 == 0:
        return False

    # Check if num is a multiple of 11
    if num % 11 == 0:
        return False

    # If num is not a multiple of any of the numbers from 2 to 11, it must be prime
    return True

def is_left_right_truncatable_prime(num):
    # Check if num contains the digit 0
    if '0' in str(num):
        return False

    # Initialize a list to store the digits of num in reverse order
    reverse_digits = []

    # Iterate through the digits of num in reverse order
    for digit in str(num)[::-1]:
        # Add each digit to the list of reverse digits
        reverse_digits.append(digit)

    # Check if all the digits in reverse order are prime numbers
    if all(is_prime(int(digit)) for digit in reverse_digits):
        return True

    # If any of the digits in reverse order are not prime numbers, num is not a left-and-right-truncatable prime number
    return False
