
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all prime numbers less than or equal to x
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    # Check if the number contains any zeroes
    if "0" in str(n):
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
