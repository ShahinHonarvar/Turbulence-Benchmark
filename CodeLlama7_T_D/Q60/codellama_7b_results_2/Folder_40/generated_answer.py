
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # If the number is a prime number and it meets the criteria of being left-and-right-truncatable prime number, add it to the list
        if is_prime(i) and is_left_right_truncatable_prime(i):
            primes.append(i)

    # Sort the list in descending order
    primes = sorted(primes, reverse=True)

    return primes


# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Function to check if a number is left-and-right-truncatable prime or not
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Check if the number can be divided by the leading leftmost and last rightmost digits without any remainder
    if n % int(str(n)[:1]) != 0 or n % int(str(n)[-1:]) != 0:
        return False

    return True
