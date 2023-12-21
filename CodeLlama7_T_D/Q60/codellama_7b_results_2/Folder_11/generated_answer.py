
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(i):

            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x in ascending order
    return sorted(prime_numbers)

# Function to check if a number is a prime number
def is_prime(n):

    # Check if n is greater than 1
    if n > 1:

        # Check if n is divisible by any number between 2 and n-1
        for i in range(2, n):
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and n-1, then it is a prime number
    return True

# Function to check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # Check if the number contains 0
    if '0' in str(n):
        return False

    # Check if the number is a palindrome
    if str(n) == str(n)[::-1]:

        # Remove leading leftmost and last rightmost digits from the number
        while n % 10 == 0:
            n = n // 10

        while n % 10 == 0 and n > 1:
            n = n // 10

        # Check if the remaining number is a prime number
        if is_prime(n):
            return True

    return False
