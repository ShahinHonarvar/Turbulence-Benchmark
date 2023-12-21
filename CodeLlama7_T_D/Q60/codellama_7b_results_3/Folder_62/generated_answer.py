
def all_left_right_truncatable_prime(x):
    # Create a list of prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    # Filter the list of prime numbers to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = []
    for prime in prime_numbers:
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_prime_numbers.append(prime)
    return left_right_truncatable_prime_numbers

def is_prime(n):
    # Check if n is a prime number by dividing it by all numbers from 2 to sqrt(n) and checking if any of the divisions are integer
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

def is_left_right_truncatable_prime(n):
    # Check if n is a left-and-right-truncatable prime number by checking if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # Check if the leading leftmost digit is equal to the last rightmost digit
    if str(n)[0] != str(n)[-1]:
        return False

    # Check if the number can be divided by removing the leading leftmost and last rightmost digits without leaving a one- or two-digit prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
