
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and no prime factor was found
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Create a copy of the original number
    number = n

    # Remove the leading leftmost digit and check if it remains a prime number
    while number > 0:
        number //= 10

    # Return False if the leading leftmost digit does not remain a prime number
    if not is_prime(number):
        return False

    # Create a copy of the original number
    number = n

    # Remove the last rightmost digit and check if it remains a prime number
    while number > 0:
        number %= 10

    # Return False if the last rightmost digit does not remain a prime number
    if not is_prime(number):
        return False

    # Return True if all conditions are met
    return True
