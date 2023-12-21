
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through all the prime numbers less than or equal to x
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the list of prime numbers
                prime_numbers.append(i)

    return prime_numbers

# Check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, then it is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n contains 0
    if "0" in str(n):
        # If n contains 0, then it is not a left-and-right-truncatable prime number
        return False

    # Check if the leading leftmost and last rightmost digits of n are both odd numbers
    if (str(n)[0] % 2 == 0) or (str(n)[-1] % 2 == 0)):
        # If the leading leftmost and last rightmost digits of n are not both odd numbers, then it is not a left-and-right-truncatable prime number
        return False

    # Check if n is still a prime number after removing the leading leftmost and last rightmost digits
    temp = n
    for i in range(2, int(n ** 0.5) + 1)):
        if temp % i == 0:
            # If temp is not a prime number, then n is not a left-and-right-truncatable prime number
            return False

    # If all the checks are passed, then n is a left-and-right-truncatable prime number
    return True
