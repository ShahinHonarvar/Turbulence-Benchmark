
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the numbers from 1 to x
    for i in range(1, x + 1):
        # If the number is a prime number and it is left-and-right-truncatable prime
        if is_prime(i) and is_left_right_truncatable_prime(i):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(i)

    # Return the list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n - 1
        for i in range(2, n):
            # If the number is divisible by any number between 2 and n - 1, it is not a prime number
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and n - 1, it is a prime number
    return True

# Function to check if a left-and-right-truncatable prime number exists in the specified range
def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digit
    if "0" in str(n):
        return False

    # Loop through the numbers from n to 1
    for i in range(n, 1, -1):
        # If the number is not prime, it cannot be a left-and-right-truncatable prime number
        if not is_prime(i):
            return False

        # Remove the leading leftmost and last rightmost digits of the number until it becomes one or two digits long
        while len(str(i)) > 2:
            i = int(str(i)[:-1])

    # If the number is less than or equal to x, it is a left-and-right-truncatable prime number
    return n <= x
