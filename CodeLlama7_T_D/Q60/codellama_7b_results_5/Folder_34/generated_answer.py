
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # If i is a prime number, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If i is a left-and-right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers

    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime

def is_prime(n):

    # Check if n is greater than 1

    if n > 1:

        # Iterate from 2 to the square root of n

        for i in range(2, int(n ** 0.5) + 1):

            # If n is divisible by i, it is not prime

            if n % i == 0:

                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime

    return True

# Define a function to check if a number is left-and-right-truncatable prime

def is_left_right_truncatable_prime(n):

    # Check if n contains any 0

    if '0' in str(n):

        return False



# If n does not contain any 0, check if it is a prime number

if is_prime(n):

    # If n is a prime number, check if it is left-and-right-truncatable prime number by removing the leading leftmost and last rightmost digits

    leading_leftmost = str(n)[:2]

    last_rightmost = str(n)[-2:]

    # If the leading leftmost digit is not 1, or if the last rightmost digit is not 1, it is not a left-and-right-truncatable prime number

    if leading_leftmost[0] != '1' or last_rightmost[0] != '1':

        return False
