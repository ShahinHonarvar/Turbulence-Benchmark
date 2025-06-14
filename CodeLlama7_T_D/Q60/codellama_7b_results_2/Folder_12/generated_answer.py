
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (inclusive)
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # If it is, check if it is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # If it is, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            return False

    # If no number between 2 and the square root of n divides n, it is a prime number
    return True

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digits
    if '0' in str(n):
        return False

    # Check if the number remains a prime number after the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(len(str(n)) - 1, 0, -1)):
        if is_prime(int(str(n)[:i] + str(n)[i+1:])):
            return True

    # If the number does not remain a prime number after the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime, it is not a left-and-right-truncatable prime number
    return False
