
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through all prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is prime or not
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Iterate from 2 to n-1
        for i in range(2, n):

            # If n is divisible by i, it is not prime
            if n % i == 0:

                # Return False
                return False

    # If n is greater than 1 and is not divisible by any number between 2 and n-1, it is prime
    return True

# Check if a number is left-and-right-truncatable prime or not
def is_left_right_truncatable_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Initialize an empty string to store the number in string format
        num_str = ""

        # Convert the number into a string
        for i in range(0, len(str(n)))):

            # Add each digit of the number to the string
            num_str += str(n)[i]

        # Check if the number is left-and-right-truncatable prime by removing the leading and last digits one at a time
        for i in range(1, len(num_str) - 1):

            # Remove the ith digit from the string
            num_str = num_str[:i] + num_str[i + 1:]

            # Check if the number is prime after removing the ith digit
            if is_prime(int(num_str)):

                # Return True
                return True

    # If n is not greater than 1, it is not left-and-right-truncatable prime
    return False
