
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all numbers from 1 to x
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
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
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

    # Check if the number contains no 0
    if "0" not in s:
        # Loop through all numbers from the length of the string to 1
        for i in range(len(s), 0, -1):
            # Check if removing the leading leftmost and last rightmost digits makes the number a prime number
            if is_prime(int(s[:i] + s[i+1:])):
                # Return True if removing the leading leftmost and last rightmost digits makes the number a prime number
                return True
    # Return False if the number contains 0 or removing the leading leftmost and last rightmost digits does not make the number a prime number
    return False
