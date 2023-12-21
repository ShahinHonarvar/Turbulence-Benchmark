
def all_right_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[32]
    prime_numbers = []

    # Check if the number is a right-truncatable prime number
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of all right-truncatable prime numbers less than x
    return prime_numbers

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False

    while n > 10:
        n = int(str(n)[:-1])

    for i in range(2, x):
        if is_prime(i) and str(n)[-1] == str(i)[-1]:
            return True

    return False
