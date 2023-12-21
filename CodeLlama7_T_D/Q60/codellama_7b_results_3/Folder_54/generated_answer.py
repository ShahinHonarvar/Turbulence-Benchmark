
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # Add the prime number to the list of prime numbers
                prime_numbers.append(num)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

def is_prime(num):

    # Check if the number is less than or equal to 1
    if num <= 1:
        return False

    # Check if the number is divisible by 2 to num - 1
    for i in range(2, num):
        if num % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by 2 to num - 1, it is prime
    return True

def is_left_right_truncatable_prime(num):

    # Check if the number contains any zeroes
    if '0' in str(num):
        return False

    # Check if the number is left-truncatable prime by removing the leading digit and checking if it is a prime number
    if is_prime(int(str(num)[1:])):

        # Check if the number is right-truncatable prime by removing the last rightmost digit and checking if it is a prime number
        if is_prime(int(str(num)[:-1])))

            return True

    return False
