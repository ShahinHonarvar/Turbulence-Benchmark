
def all_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the range of numbers from 1 to x - 1
    for i in range(1, x - 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is a right-truncatable prime number
            if is_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):

    # Check if the number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the number is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by 2 to n - 1, it is a prime number
    return True

# Check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):

    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Loop through the range of numbers from 1 to n - 1
    for i in range(1, n - 1):

        # Check if the number is divisible by the last rightmost digit
        if n % (n // 10 ** i) == 0:
            return False

    # If the number is a prime number and it is not divisible by the last rightmost digit, it is a right-truncatable prime number
    return True
