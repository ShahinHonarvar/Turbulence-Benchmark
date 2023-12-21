
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    rtp = []

    # Loop through each integer in the tuple

    for x in tuple:

        # Check if x is a prime number

        if is_prime(x):

            # Check if x is a right-truncatable prime number

            if is_rtp(x):

                # Add x to the list of right-truncatable prime numbers

                rtp.append(x)

    # Sort the list of right-truncatable prime numbers in descending order

    rtp = sorted(rtp, reverse=True)

    # Return the list of right-truncatable prime numbers

    return rtp

# Check if a number is a prime number

def is_prime(n):

    # Return True if n is a prime number and False otherwise

    if n == 1:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True

# Check if a number is a right-truncatable prime number

def is_rtp(n):

    # Return True if n is a right-truncatable prime number and False otherwise

    if not is_prime(n):

        return False

    while n > 1:

        last_digit = n % 10

        n //= 10

        if last_digit == 0 or n % last_digit == 0:

            return False

    return True
