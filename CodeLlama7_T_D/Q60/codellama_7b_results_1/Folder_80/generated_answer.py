 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []
    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is prime
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add the number to the result list
                result.append(i)
    # Sort the result list in descending order
    result.sort(reverse=True)
    return result

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and is not divisible by 2 to n-1, it is prime
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is a left-and-right-truncatable prime

    # Check if n contains no 0
    if "0" in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.

    # Initialize a variable to store the number that is created by removing the leading leftmost digit of n
    num = int(str(n)[1:]))
    # Check if num is less than or equal to 9 and is a prime number
    while num <= 9 and is_prime(num):
        # If num is less than or equal to 9 and is a prime number, it is a left-and-right-truncatable prime number. Return True
        return True

    # Initialize a variable to store the number that is created by removing the last rightmost digit of n
    num = int(str(n)[:-1]))
    # Check if num is less than or equal to 9 and is a prime number
    while num <= 9 and is_prime(num):
        # If num is less than or equal to 9 and is a prime number, it is a left-and-right-truncatable prime number. Return True
        return True

    # If the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime, it is not a left-and-right-truncatable prime number. Return False
    return False
