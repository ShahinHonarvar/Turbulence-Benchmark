
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the left-truncatable prime numbers
    leftTruncatablePrimes = []

    # Loop through each number in the tuple

    for i in range(len(tuple)):

        # Set the current number as x

        x = tuple[i]

        # Check if x is a prime number

        if is_prime(x):

            # Initialize an empty list to store the digits of x

            digitsOfX = []

            # Loop through each digit in the string representation of x

            for digit in str(x):

                # Append the digit to the digitsOfX list

                digitsOfX.append(digit)

            # Initialize an empty string to store the left-truncatable prime numbers less than x

            leftTruncatablePrimesStr = ""

            # Loop through each digit in the reverse order of the digits of x

            for digit in reversed(digitsOfX):

                # If the current digit is not 0, append it to the leftTruncatablePrimesStr string

                if digit != "0":

                    leftTruncatablePrimesStr += digit

            # Check if the integer value of the leftTruncatablePrimesStr string is a prime number

            if is_prime(int(leftTruncatablePrimesStr)):

                # Add x to the list of left-truncatable prime numbers

                leftTruncatablePrimes.append(x)

    # Return the sorted list of all left-truncatable prime numbers less than x

    return sorted(leftTruncatablePrimes, reverse=True)

# Check if a number is a prime number

def is_prime(n):

    # If n is not an integer, return False

    if not isinstance(n, int):

        return False

    # If n is less than 2, return False

    if n < 2:

        return False

    # If any number between 2 and the square root of n is divisible by it, return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    # If none of the numbers between 2 and the square root of n are divisible by it, return True

    return True
