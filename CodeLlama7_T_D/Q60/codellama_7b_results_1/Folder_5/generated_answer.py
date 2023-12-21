 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_list.append(i)
    # Sort the list of prime numbers in ascending order
    prime_list.sort()
    return prime_list

def is_prime(n):
    """Check if a number is prime"""
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

    # Return True if n is prime
    return True

def is_left_right_truncatable_prime(n):
    """Check if a number is a left-and-right-truncatable prime number"""
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    # Initialize the leading leftmost digit of n as the first digit in the string representation of n
    leading_leftmost_digit = str(n)[0]
    # Initialize the last rightmost digit of n as the last digit in the string representation of n
    last_rightmost_digit = str(n)[-1]
    # Initialize a variable to store the number formed by removing the leading leftmost and last rightmost digits from n
    num = n

    while True:
        # Check if the number formed by removing the leading leftmost and last rightmost digits from num is greater than 1
        if str(num)[0:-2] > 1:
            # Return False if the number formed by removing the leading leftmost and last rightmost digits from num is greater than 1
            return False

        # Check if the number formed by removing the leading leftmost and last rightmost digits from num is less than or equal to 1
        elif str(num)[0:-2] <= 1:
            # Check if the number formed by removing the leading leftmost and last rightmost digits from num is a prime number
            if is_prime(str(num)[0:-2])):
                # Return True if the number formed by removing the leading leftmost and last rightmost digits from num is a prime number
                return True
