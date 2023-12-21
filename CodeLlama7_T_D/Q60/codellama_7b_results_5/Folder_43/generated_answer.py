
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list for storing the prime numbers
    prime_list = []

    # Iterate over each element in the tuple
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # If it is, check if it is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(element):
                # If it is, add it to the list of prime numbers
                prime_list.append(element)

    # Sort the list in descending order and return it
    return sorted(prime_list, reverse=True)

# Define a function for checking if a number is a prime number
def is_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        # If it is not, return False
        return False

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            # If it does, return False
            return False

    # If no divisor was found, return True
    return True

# Define a function for checking if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        # If it is not, return False
        return False

    # Check if n is a prime number
    if not is_prime(n):
        # If it is not, return False
        return False

    # Iterate over the digits of n in reverse order
    for digit in str(n)[::-1]:
        # Check if the current digit is 0
        if digit == '0':
            # If it is, return False
            return False

    # If no divisor was found and the number has no 0 digits, return True
    return True
