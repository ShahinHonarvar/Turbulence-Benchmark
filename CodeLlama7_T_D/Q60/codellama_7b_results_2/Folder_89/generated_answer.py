
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
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
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is a prime number
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Convert the number to a string
    s = str(n)

    # Check if the string contains any 0
    for c in s:
        if c == '0':
            # Return False if the string contains any 0
            return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, len(s)):
        # Check if the number is a prime number after removing the leading leftmost digit
        if is_prime(int(s[i:])):
            # Check if the number is a prime number after removing the last rightmost digit
            if is_prime(int(s[:-i])))
                return True
    return False
