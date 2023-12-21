 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Iterate through all the prime numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if the current number is a prime number
        if is_prime(i):
            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the prime list
                prime_list.append(i)
    # Sort the prime list in ascending order
    prime_list.sort()
    # Return the sorted prime list
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, return False
        return False

    # Initialize an empty string to store the digits of n
    digits = ""

    # Iterate through all the digits of n
    for digit in str(n):
        # Check if the current digit is not 0
        if digit != "0":
            # Add the current digit to the digits string
            digits += digit

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number
    for i in range(1, len(digits) + 1):
        # Check if the current number of digits is greater than or equal to 2
        if len(digits) >= 2:
            # Check if the current number is a prime number
            if is_prime(int(digits[:len(digits) - i])):
                # If the current number is a prime number, return True
                return True
