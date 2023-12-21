
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_numbers.append(i)

    return prime_numbers

def is_prime(n):

    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return False

    # Check if n is an odd number
    if n % 2 == 0:
        return False

    # Check if n has any prime factors other than 2 and 3
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if n has no leading leftmost and last rightmost digits
    if len(str(n)) > 2:
        return False

    # Check if n remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[i:] + str(n)[:i]))):
            return False

    return True
