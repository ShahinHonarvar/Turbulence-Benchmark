
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the range of numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if the number is less than or equal to 1
    if n <= 1:

        # Return False if the number is less than or equal to 1
        return False

    # Check if the number is divisible by 2 to n - 1
    for i in range(2, n):

        # Check if the number is divisible by i
        if n % i == 0:

            # Return False if the number is divisible by i
            return False

    # Return True if the number is a prime number
    return True

# Define a function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):

    # Check if the number is less than or equal to 1
    if n <= 1:

        # Return False if the number is less than or equal to 1
        return False

    # Check if the number contains no 0
    if "0" in str(n):

        # Return False if the number contains no 0
        return False

    # Check if the number remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, len(str(n)))):

        # Remove the leading leftmost digit of the number
        n = int(str(n)[i:] + str(n)[:i]))

        # Check if the number is a one- or two-digit prime
        if is_prime(n):

            # Return True if the number is a one- or two-digit prime
            return True

    # Return False if the number does not meet the criteria for being a left-and-right-truncatable prime
    return False
