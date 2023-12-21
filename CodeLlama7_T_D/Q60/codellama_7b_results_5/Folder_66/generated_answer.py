
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number (inclusive)
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any number between 2 and the square root of the number
            if n % i == 0:
                # If the number is divisible by any number between 2 and the square root of the number, it is not a prime number
                return False

    # If the number is greater than 1 and is not divisible by any number between 2 and the square root of the number, it is a prime number
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Convert the number to string
    s = str(n)

    # Check if the number contains no 0
    if "0" not in s:
        # Iterate from the length of the string (exclusive) to 1 (inclusive)
        for i in range(len(s), 0, -1):
            # Check if the number is still prime after removing the leading leftmost and last rightmost digits
            if is_prime(int(s[:i] + s[i+1:])):
                # If the number is still prime after removing the leading leftmost and last rightmost digits, it is a left-and-right-truncatable prime number
                return True

    # If the number contains 0 or is not left-and-right-truncatable prime number, it is not a left-and-right-truncatable prime number
    return False
