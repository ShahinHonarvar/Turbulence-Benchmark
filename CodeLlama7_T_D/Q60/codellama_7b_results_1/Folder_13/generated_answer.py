
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Loop through all the numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the left-and-right-truncatable prime number to the list
                prime_list.append(i)
    return prime_list

def is_prime(n):
    # Check if n is less than 2 or not an integer
    if n < 2 or not isinstance(n, int):
        # Return False if n is less than 2 or not an integer
        return False

    # Loop through all the numbers less than or equal to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n without leaving a remainder
        if n % i == 0:
            # Return False if i divides n without leaving a remainder
            return False

    # If the loop completes successfully, return True
    return True

def is_left_right_truncatable_prime(n):
    # Check if n is less than 2 or not an integer
    if n < 2 or not isinstance(n, int):
        # Return False if n is less than 2 or not an integer
        return False

    # Loop through all the numbers less than or equal to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n without leaving a remainder
        if n % i == 0:
            # Return False if i divides n without leaving a remainder
            return False

    # If the loop completes successfully, return True
    return True
