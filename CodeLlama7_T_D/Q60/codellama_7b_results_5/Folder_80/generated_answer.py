
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to x
    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left- and right-truncatable prime
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

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
                # Return False if a factor is found
                return False

    # If n is a prime number, return True
    return True

# Check if a number is left- and right-truncatable prime
def is_left_right_truncatable_prime(n):
    # Check if n contains any 0 digits
    if '0' in str(n):
        # Return False if n contains any 0 digits
        return False

    # Iterate from the leftmost to the rightmost digits of n
    for i in range(len(str(n)))):
        # Check if the digit at position i is not equal to the digit at position len(str(n))) - i
        if str(n)[i] != str(n)[len(str(n)) - i]:
            # Return False if a mismatching digit is found
            return False

    # If no mismatching digits are found, return True
    return True
