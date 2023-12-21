
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through all integers from 1 to x
    for i in range(1, x + 1):
        # Check if the integer is a prime number
        if is_prime(i):
            # Check if the integer can be divided by 10 without leaving a one-digit number
            if (i % 10) == 0 and (i // 10) in range(10):
                # Add the integer to the list of prime numbers
                prime_numbers.append(i)

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is a prime number
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Loop through all integers from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the number is divisible by any integer between 2 and the square root of the number
            if n % i == 0:
                # Return False if the number is divisible by any integer between 2 and the square root of the number
                return False

    # If the number is less than or equal to 1, it is not a prime number
    else:
        # Return False if the number is less than or equal to 1
        return False
