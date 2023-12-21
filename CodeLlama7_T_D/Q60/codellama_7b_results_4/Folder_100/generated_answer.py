
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate through the numbers from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_list.append(i)
    return prime_list

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Check if n is an odd number
    if n % 2 == 0:
        return False

    # Use the Sieve of Eratosthenes to find all prime numbers up to n
    sieve = [True] * (n + 1)
    for p in range(3, int(n ** 0.5) + 1, 2):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return any(sieve[i] for i in range(3, n + 1, 2)))

def left_right_truncatable_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # Check if the number contains no 0
    if "0" in str(n):
        return False

    # Check if the number is left-and-right-truncatable prime number
    for i in range(len(str(n))):
        # Remove the leading leftmost digit
        n = int(str(n)[1:])
        # Check if the remaining number is a prime number
        if not is_prime(n):
            return False

        # Remove the last rightmost digit
        n = int(str(n)[:-1])
        # Check if the remaining number is a prime number
        if not is_prime(n):
            return False

    return True
