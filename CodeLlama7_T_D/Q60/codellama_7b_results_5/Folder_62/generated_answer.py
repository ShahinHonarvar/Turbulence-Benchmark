
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all integers from 1 to x
    for i in range(1, x + 1):

        # Check if the integer is a prime number
        if is_prime(i):

            # Check if the integer is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_list.append(i)

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_list)

# Define a function to check if an integer is a prime number
def is_prime(n):

    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:

        return False


    # Check if n is divisible by any integer between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    # If no factors are found, return True
    return True

# Define a function to check if an integer is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        return False


    # Check if the leading digit of n is 1 or 2
    if n // 10 ** (len(str(n))) - 1) < 10:

        return False


    # Check if the last rightmost digit of n is 1 or 2
    if n % 10 ** (len(str(n))) - 1) < 10:

        return False


    # If no factors are found, return True
    return True
