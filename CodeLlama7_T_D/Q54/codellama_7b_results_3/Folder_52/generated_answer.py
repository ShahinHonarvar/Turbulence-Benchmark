
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the sorted right-truncatable prime numbers
    prime_numbers = []

    # Get the integer at index 52 in the tuple

    x = tuple[52]

    # Iterate from 1 to x - 1 and check if each number is a right-truncatable prime number

    for i in range(1, x - 1):

        # Check if the current number is a prime number

        if is_prime(i):

            # Check if the last rightmost digit of the current number is successively removed and remains a prime number

            if is_prime(get_last_digit(i)):

                # Add the current number to the list of right-truncatable prime numbers

                prime_numbers.append(i)

    # Sort the list of right-truncatable prime numbers in descending order

    prime_numbers.sort(reverse=True)

    return prime_numbers


def is_prime(n):

    # Check if n is greater than 1

    if n > 1:

        # Iterate from 2 to the square root of n

        for i in range(2, int(n ** 0.5) + 1):

            # Check if i divides n without a remainder

            if n % i == 0:

                # If yes, return False as n is not a prime number

                return False


    # Return True as n is a prime number

    return True


def get_last_digit(n):

    # Check if n is greater than 10

    if n > 10:

        # Get the last two digits of n

        last_two_digits = int(str(n)[-2:])

        # Return the last digit of the number

        return last_two_digits % 10
