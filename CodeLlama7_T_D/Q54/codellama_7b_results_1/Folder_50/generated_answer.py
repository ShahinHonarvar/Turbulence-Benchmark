
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate over the tuple of integers
    for i in tuple:

        # Check if the current integer is a prime number
        if is_prime(i):

            # If the current integer is a prime number, check if it is a right-truncatable prime number
            if is_right_truncatable_prime(i):

                # If the current integer is a right-truncatable prime number, add it to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in descending order
    prime_list.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_list

# Check if a given integer is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:

        # If n is less than or equal to 1, it is not a prime number
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):

        # If n is divisible by i, it is not a prime number
        if n % i == 0:

            return False

    # If n is greater than 1 and it is not divisible by 2 to n-1, it is a prime number
    return True

# Check if a given integer is a right-truncatable prime number
def is_right_truncatable_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:

        # If n is less than or equal to 1, it is not a right-truncatable prime number
        return False

    # Check if the last digit of n is a prime number
    if is_prime(n % 10) == False:

        # If the last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the second to last digit of n is a prime number
    if is_prime((n % 100) / 10) == False:

        # If the second to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the third to last digit of n is a prime number
    if is_prime((n % 1000) / 100) == False:

        # If the third to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the fourth to last digit of n is a prime number
    if is_prime((n % 10000) / 1000) == False:

        # If the fourth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the fifth to last digit of n is a prime number
    if is_prime((n % 100000) / 10000) == False:

        # If the fifth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the sixth to last digit of n is a prime number
    if is_prime((n % 1000000) / 100000) == False:

        # If the sixth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the seventh to last digit of n is a prime number
    if is_prime((n % 10000000) / 1000000) == False:

        # If the seventh to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the eighth to last digit of n is a prime number
    if is_prime((n % 100000000) / 100000000) == False:

        # If the eighth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the ninth to last digit of n is a prime number
    if is_prime((n % 1000000000) / 10000000000) == False:

        # If the ninth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the tenth to last digit of n is a prime number
    if is_prime((n % 10000000000) / 100000000000) == False:

        # If the tenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the eleventh to last digit of n is a prime number
    if is_prime((n % 100000000000) / 1000000000000) == False:

        # If the eleventh to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the twelvth to last digit of n is a prime number
    if is_prime((n % 1000000000000) / 10000000000000) == False:

        # If the twelvth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the thirteenth to last digit of n is a prime number
    if is_prime((n % 10000000000000) / 100000000000000) == False:

        # If the thirteenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the fourteenth to last digit of n is a prime number
    if is_prime((n % 100000000000000) / 1000000000000000) == False:

        # If the fourteenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the fifteenth to last digit of n is a prime number
    if is_prime((n % 1000000000000000) / 10000000000000000) == False:

        # If the fifteenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the sixteenth to last digit of n is a prime number
    if is_prime((n % 10000000000000000) / 100000000000000000) == False:

        # If the sixteenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the seventeenth to last digit of n is a prime number
    if is_prime((n % 100000000000000000) / 1000000000000000000) == False:

        # If the seventeenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the eighteenth to last digit of n is a prime number
    if is_prime((n % 100000000000000000) / 1000000000000000000) == False:

        # If the eighteenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the nineteenth to last digit of n is a prime number
    if is_prime((n % 100000000000000000) / 1000000000000000000) == False:

        # If the nineteenth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the twentieth to last digit of n is a prime number
    if is_prime((n % 100000000000000000) / 1000000000000000000) == False:

        # If the twentieth to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the twenty-first to last digit of n is a prime number
    if is_prime((n % 100000000000000000) / 10000000000000000000) == False:

        # If the twenty-first to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the twenty-second to last digit of n is a prime number
    if is_prime((n % 1000000000000000000) / 100000000000000000000) == False:

        # If the twenty-second to last digit of n is not a prime number, it is not a right-truncatable prime number
        return False

    # Check if the twenty-third to last digit of n is a prime number
    if is_prime((n % 1000000000000000000) / 1000000000000000000000) == False:

        # If the twenty-third to last digit of n is not a prime number, it is not a right-truncatable prime number

    return True
