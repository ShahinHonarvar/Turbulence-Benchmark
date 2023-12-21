
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all the numbers from 1 to x
    for num in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(num):
            # If the number is prime, check if it is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(num):
                # If the number is left-and-right-truncatable prime, add it to the list of prime numbers
                prime_numbers.append(num)
    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If n is less than or equal to 1, return False
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        # If n is divisible by i, return False
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

# Function to check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        # If n is less than or equal to 1, return False
        return False

    # Check if n contains any 0 digits
    if '0' in str(n):
        # If n contains any 0 digits, return False
        return False

    # Check if the leading leftmost and last rightmost digits of n are not equal to each other
    if str(n)[0] == str(n)[-1]:
        # If the leading leftmost and last rightmost digits of n are not equal to each other, return False
        return False

    # Check if the number formed by removing the leading leftmost digit of n is prime
    if is_prime(int(str(n))[1:])):
        # If the number formed by removing the leading leftmost digit of n is prime, check if the number formed by removing the last rightmost digit of n is prime
        if is_prime(int(str(n)))[:-1]):
            # If the number formed by removing the last rightmost digit of n is prime, return True
            return True

    # If the loop completes successfully and no prime number is found, return False
    return False
