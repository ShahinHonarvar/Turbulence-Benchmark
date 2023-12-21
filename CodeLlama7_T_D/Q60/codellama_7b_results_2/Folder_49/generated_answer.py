
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

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):

    # Check if the number is less than or equal to 1
    if n <= 1:

        # The number is not a prime number
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1)):

        # Check if the number is divisible by i
        if n % i == 0:

            # The number is not a prime number
            return False

    # The number is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains any 0 digits
    if '0' in str(n):

        # The number is not a left-and-right-truncatable prime number
        return False

    # Check if the number is divisible by any number between 1 and the square root of the number
    for i in range(1, int(n ** 0.5) + 1)):

        # Check if the number is divisible by i
        if n % i == 0:

            # The number is not a left-and-right-truncatable prime number
            return False

    # The number is a left-and-right-truncatable prime number
    return True
