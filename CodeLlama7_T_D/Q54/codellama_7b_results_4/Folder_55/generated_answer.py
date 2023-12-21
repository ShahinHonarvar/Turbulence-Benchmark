
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    right_truncatable_primes = []

    # Iterate over the tuple of positive integers

    for x in tuple:

        # Check if x is a prime number

        if is_prime(x):

            # Initialize an empty string to store the last rightmost digit of x

            last_rightmost_digit = ""

            # Loop until the last rightmost digit of x becomes 0

            while last_rightmost_digit != "0":

                # Extract the last rightmost digit of x and assign it to last_rightmost_digit

                last_rightmost_digit = str(x % 10)

                # Remove the last rightmost digit of x from x

                x //= 10


                # Check if x is a prime number


                if not is_prime(x):

                    # If x is not a prime number, break the loop and move on to the next value of x in the tuple

                    break


            # If last_rightmost_digit becomes 0, it means that all digits of x have been removed, and x is still a prime number. In this case, add x to the list of right-truncatable prime numbers.

            if last_rightmost_digit == "0":

                right_truncatable_primes.append(x)


    # Return the sorted list of all right-truncatable prime numbers less than x. The returned list should be sorted in descending order.

    return sorted(right_truncatable_primes, reverse=True)

# Define a function to check if a number is a prime number

def is_prime(n):

    # Check if n is greater than 1

    if n > 1:

        # Loop from 2 to the square root of n

        for i in range(2, int(n ** 0.5) + 1)):

            # Check if i divides n

            if n % i == 0:

                # If i divides n, return False

                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is a prime number. Return True.

    return True
