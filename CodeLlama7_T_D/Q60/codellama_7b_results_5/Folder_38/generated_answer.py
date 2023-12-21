
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number is not one or two digits
    if len(str(n)) > 2:
        # Check if the leading digit and last rightmost digit are both different from 0
        if str(n)[0] != "0" and str(n)[-1] != "0":
            # Check if the number is still prime after removing the leading leftmost and last rightmost digits
            if is_prime(int(str(n)[:-1]) + int(str(n)[2:]))) == True:
                # Return True if the number is left-and-right-truncatable prime number
                return True

    # Return False if the number is not left-and-right-truncatable prime number
    return False
