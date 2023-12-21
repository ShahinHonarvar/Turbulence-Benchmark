
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                primes.append(i)

    # Return the sorted list of prime numbers
    return sorted(primes)

# Check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # Return False if n is less than or equal to 1
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # If n is divisible by i, return False
        if n % i == 0:
            return False

    # Return True if n is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains 0
    if "0" in str(n):
        # Return False if the number contains 0
        return False

    # Check if the number is a prime number
    if not is_prime(n):
        # Return False if the number is not a prime number
        return False

    # Remove the leading leftmost and last rightmost digits of the number
    leading_leftmost = str(n)[:-1]
    last_rightmost = str(n)[1:]

    # Check if the number remains prime after removing the leading leftmost and last rightmost digits
    if is_prime(int(leading_leftmost)) and is_prime(int(last_rightmost)):
        # Return True if the number remains prime after removing the leading leftmost and last rightmost digits
        return True

    # Return False if the number does not remain prime after removing the leading leftmost and last rightmost digits
    return False
