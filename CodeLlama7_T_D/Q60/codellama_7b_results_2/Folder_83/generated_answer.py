
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the prime number to the list
                prime_list.append(i)

    # Sort the list in ascending order
    prime_list.sort()

    # Return the sorted list of left-and-right-truncatable prime numbers less than or equal to x
    return prime_list

# Check if a number is a prime number using the Sieve of Eratosthenes
def is_prime(n):

    # If the number is less than 2, it is not a prime number
    if n < 2:
        return False

    # Mark all numbers up to the square root of n as composite
    sieve = [True] * (n + 1)
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p ** 2, n + 1, p):
                sieve[i] = False

    # Return True if the number is a prime number, and False otherwise
    return sieve[n]

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # If the number contains 0, it is not a left-and-right-truncatable prime number
    if '0' in str(n):
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        return False

    # Remove the leading and last digits of the number repeatedly until it becomes a one- or two-digit prime number
    while n > 10:
        n = int(str(n)[:-1] + str(n)[-1]))

        # If the number is not a prime number, it is not a left-and-right-truncatable prime number
        if not is_prime(n):
            return False

    # Return True if the number is a left-and-right-truncatable prime number, and False otherwise
    return n == 1 or n == 2 or n == 3 or n == 5 or n == 7
