
def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 2 to n-1 (excluding n)
    for i in range(2, n):

        # Check if i is a prime number
        if is_prime(i):

            # Check if the last digit of i is a right-truncatable prime number
            if is_right_truncatable_prime(i):
                prime_numbers.append(i)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of all right-truncatable prime numbers less than n
    return prime_numbers

# Function to check if a number is prime or not
def is_prime(n):
    # Initialize a variable as 1
    i = 1

    # Check if any number between 2 and the square root of n divides n without leaving a remainder
    while i * i <= n:
        if n % i == 0:
            return False

        # Increment i by 1
        i += 1

    # If no number between 2 and the square root of n divides n, then it is prime
    return True

# Function to check if a number is a right-truncatable prime number or not
def is_right_truncatable_prime(n):
    # Initialize a variable as n
    i = n

    # Check if the last digit of i is a prime number
    while i > 0:
        if not is_prime(i % 10):
            return False

        # Divide i by 10
        i //= 10

    # If the last digit of i is a right-truncatable prime number, then it is a right-truncatable prime number
    return True
