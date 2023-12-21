
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:
                # Return False if the number is divisible by any number between 2 and the square root of the number
                return False

    # Return True if the number is greater than 1 and not divisible by any number between 2 and the square root of the number
    return n > 1

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains no 0
    if "0" not in str(n):
        # Iterate from the leading digit to the last rightmost digit
        for i in range(1, len(str(n)))):
            # Check if the number is still prime after removing the leading leftmost and last rightmost digits
            if is_prime(int(str(n)[:i] + str(n)[i+1:]))) :
                # Return True if the number is still prime after removing the leading leftmost and last rightmost digits
                return True

    # Return False if the number contains 0 or is not still prime after removing the leading leftmost and last rightmost digits
    return False
