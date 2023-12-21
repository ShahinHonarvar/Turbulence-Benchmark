
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the tuple of positive integers
    for i in tuple:
        # Check if the number is a prime number
        if is_prime(i):
            # If it is a prime number, check if it is a right-truncatable prime number
            if is_right_truncatable_prime(i):
                # If it is a right-truncatable prime number, add it to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n-1
        for i in range(2, n):
            # If the remainder of dividing n by i is equal to 0, return False
            if n % i == 0:
                return False

    # If the number is greater than 1 and has no factors other than 1 and itself, return True
    return True

# Function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Initialize an empty string to store the last rightmost digit of the number
    last_digit = ""

    # Loop through the numbers from n to 1
    for i in range(n, 0, -1):
        # If the remainder of dividing n by i is equal to 0, return False
        if n % i == 0:
            return False

        # Check if the last rightmost digit of the number is equal to the last rightmost digit of the current number
        if str(i)[-1:] != last_digit:
            last_digit = str(i)[-1:]

    # If the number is greater than 1 and has no factors other than 1 and itself, return True
    return True
