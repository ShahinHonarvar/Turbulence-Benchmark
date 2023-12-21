
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is a left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    return prime_numbers


# Check if a number is a prime number
def is_prime(n):
    # A prime number is greater than 1 and has only two factors: 1 and itself
    if n > 1:
        # Iterate from 2 to the square root of n, inclusive
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not a prime number
                return False

    # If the loop completes without returning False, then n is a prime number
    return True


# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # A left-and-right-truncatable prime number is a prime number that contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.

    # Check if n is a prime number
    if not is_prime(n):
        # If n is not a prime number, then it is not a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost digit of n is 0
    if str(n)[0] == "0":
        # If the leading leftmost digit of n is 0, then n is not a left-and-right-truncatable prime number
        return False

    # Check if the last rightmost digit of n is 0
    if str(n)[-1] == "0":
        # If the last rightmost digit of n is 0, then n is not a left-and-right-truncatable prime number
        return False

    # Check if n is divisible by the leading leftmost digit of n
    if int(str(n)[0]) != 0 and n % int(str(n)[0])):
        # If n is not divisible by the leading leftmost digit of n, then n is not a left-and-right-truncatable prime number
        return False

    # Check if n is divisible by the last rightmost digit of n
    if int(str(n)[-1])):
        # If n is not divisible by the last rightmost digit of n, then n is not a left-and-right-truncatable prime number
        return False

    # If all checks have passed, then n is a left-and-right-truncatable prime number
    return True
