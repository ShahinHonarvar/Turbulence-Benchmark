
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through all the numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if the number is a prime number using the Sieve of Eratosthenes algorithm
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number using the Sieve of Eratosthenes algorithm
def is_prime(n):

    # If the number is less than 2, it is not prime
    if n < 2:
        return False

    # Mark all the multiples of n as composite in an array
    sieve = [True] * (n + 1)

    # Set the number itself as composite
    sieve[n] = False

    # Iterate through all the numbers up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):

        # If the current number is marked as prime, then mark all its multiples as composite
        if sieve[i]:
            sieve[i * i:n + 1:i] = [False] * ((n + 1 - i * i) // i)

    # Return True if the number is prime, else return False
    return sieve[n]

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # If the number is not a prime number, then it cannot be a left-and-right-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the number remains prime after removing the leading leftmost and last rightmost digits
    if is_prime(n % 10) and is_prime(n // 10)):
        return True

    # Return False if the number does not meet the criteria of being a left-and-right-truncatable prime number
    return False
