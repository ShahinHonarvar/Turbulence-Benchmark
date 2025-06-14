
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # Check if the current number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the current number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

def is_left_right_truncatable_prime(n):
    # Check if the current number contains 0
    if '0' in str(n):
        return False

    # Remove the leading leftmost and last rightmost digits from the current number
    leading_digits = str(n)[:2]
    trailing_digits = str(n)[-2:]

    # Check if the current number remains prime after removing the leading leftmost and last rightmost digits
    if is_prime(int(leading_digits)) and is_prime(int(trailing_digits)):
        return True

    else:

        # Return False if the current number does not remain a prime number after removing the leading leftmost and last rightmost digits
        return False

def is_prime(n):

    # Check if the current number is equal to 1 or less than 1
    if n <= 1:
        return False

    # Check if the current number is equal to 2 or greater than 2
    if n == 2:
        return True

    # Check if the current number is odd and not divisible by 3, 5, or 7
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    # Check if the current number is prime using the Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):

        # Check if the current number is divisible by any number between 2 and the square root of the current number
        if n % i == 0:

            # Return False if the current number is divisible by any number between 2 and the square root of the current number
            return False

    # Return True if the current number is prime
    return True
