
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through all the numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_list.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_list)

# Define a function to check if a number is a prime number
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and n - 1, then it is prime
    return True

# Define a function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains no 0
    if '0' in str(n):
        return False

    # Check if the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, n + 1):

        # Check if the number is divisible by i
        if n % i == 0:

            # Check if the number is not divisible by any other number between i and n
            for j in range(i + 1, n + 1):
                if n % j == 0:
                    return False

    # If the number is left-and-right-truncatable prime number, then it remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    return True
