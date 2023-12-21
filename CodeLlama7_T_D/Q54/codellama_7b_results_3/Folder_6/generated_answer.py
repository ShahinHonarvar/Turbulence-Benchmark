
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    prime_numbers = []

    # Loop through each element in the tuple

    for x in tuple:

        # Check if x is a prime number

        if is_prime(x):

            # Initialize an empty string to store the rightmost digit of x

            rightmost_digit = ""

            # Loop through each character in the string representation of x

            for char in str(x):

                # Check if char is the last character in the string representation of x

                if char == str(x)[-1]:

                    # Add char to the rightmost_digit string

                    rightmost_digit += char

                    # Check if the integer value of rightmost_digit is prime

                    if is_prime(int(rightmost_digit)):

                        # Add x to the list of prime numbers

                        prime_numbers.append(x)

            # Return the sorted list of prime numbers

            return sorted(prime_numbers)

# Check if a number is prime by dividing it by all positive integers less than or equal to its square root

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True
