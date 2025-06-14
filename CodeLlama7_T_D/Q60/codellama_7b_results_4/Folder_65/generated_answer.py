
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the current number to the list of prime numbers
                prime_list.append(i)

    # Sort the list of prime numbers in ascending order
    prime_list.sort()

    # Return the list of prime numbers
    return prime_list

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:

        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):

            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number, then it is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Check if the number contains no 0
    if "0" in str(n):
        return False

    # Iterate from 1 to the square root of the number
    for i in range(1, int(n ** 0.5) + 1):

        # Check if the number is divisible by any number between 1 and the square root of the number
        if n % i == 0:
            return False

    # If the number is a prime number that contains no 0 and it is not divisible by any number between 1 and the square root of the number, then it is a left-and-right-truncatable prime number
    return True
