
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Loop through all prime numbers less than or equal to x
    for i in range(2, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                primes.append(i)

    # Sort the list of prime numbers in ascending order
    primes = sorted(primes)

    return primes

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If so, return False
                return False

    # If we reach this point, return True
    return True

# Check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
    # Initialize a variable to store the number of digits in n
    num_digits = len(str(n))

    # Loop through all numbers from 1 to num_digits - 1
    for i in range(1, num_digits):
        # Check if removing the leftmost digit from n results in a prime number
        if is_prime(int(str(n)[1:])))
            return True

        # Check if removing the last rightmost digit from n results in a prime number
        if is_prime(int(str(n)[:-1])))
            return True

    # If we reach this point, return False
    return False
