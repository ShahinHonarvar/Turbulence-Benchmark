
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x (both inclusive)
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            if is_left_right_truncatable_prime(i):
                # If the condition is met, add i to the list of prime numbers
                prime_numbers.append(i)
    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If none of the above conditions are met, then n is prime
    return True

# Function to check if a number is left-and-right-truncatable prime or not
def is_left_right_truncatable_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n contains any 0 digits
    if "0" in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(-int(n ** 0.5) + 1, int(n ** 0.5) + 1):
        if is_prime(n // 10 ** abs(i)) and n % 10 ** abs(i) == 0:
            return True

    # If none of the above conditions are met, then n is not a left-and-right-truncatable prime
    return False
