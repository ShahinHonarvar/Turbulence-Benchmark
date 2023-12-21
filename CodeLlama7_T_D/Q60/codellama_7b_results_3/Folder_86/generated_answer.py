
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)
    return prime_numbers

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Function to check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digit
    if "0" in str(n):
        return False

    # Check if the number is a palindrome
    if str(n) == str(n)[::-1]:
        return True

    return False
