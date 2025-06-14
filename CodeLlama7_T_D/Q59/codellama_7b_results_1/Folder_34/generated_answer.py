
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the left-truncatable prime numbers
    ltp = []

    # Iterate through the tuple and check if each element is a prime number

    for i in range(len(tuple)):
        x = tuple[i]

        # Check if x is a prime number

        if is_prime(x):

            # If x is a prime number, then check if it is left-truncatable

            if is_left_truncatable(x):
                ltp.append(x)

    return sorted(ltp, reverse=True)

# Check if a number is prime by iterating through all the numbers up to its square root and checking if any of them divide it evenly

def is_prime(n):

    # If n is less than 2, then it is not prime

    if n < 2:
        return False

    # Check if any number between 2 and the square root of n divides it evenly

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Check if a number is left-truncatable by iterating through all the numbers up to its square root and checking if any of them are prime numbers

def is_left_truncatable(n):

    # If n is less than 2, then it is not left-truncatable

    if n < 2:
        return False

    # Check if any number between 2 and the square root of n is a prime number

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime(i):
            return True

    return False
