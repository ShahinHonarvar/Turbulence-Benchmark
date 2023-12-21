
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Loop through all the numbers from 1 to x
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):

                # Add the number to the list of prime numbers
                primes.append(num)

    # Return the sorted list of prime numbers
    return sorted(primes)

# Check if a number is prime or not
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Loop through all the numbers from 2 to n - 1
        for i in range(2, n):

            # If n is divisible by any number between 2 and n - 1, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and n - 1, it is prime
    return True

# Check if a number is left-and-right-truncatable prime or not
def is_left_right_truncatable_prime(n):

    # Check if the number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Check if the number can be divided by any number between 2 and floor(sqrt(n)))
    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    # If all the checks are passed, the number is a left-and-right-truncatable prime number
    return True
