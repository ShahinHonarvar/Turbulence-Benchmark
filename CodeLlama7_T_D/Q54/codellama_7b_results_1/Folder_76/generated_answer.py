
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each element in the tuple
    for i in range(len(tuple)):
        x = tuple[i]

        # Check if x is a prime number
        if is_prime(x):

            # Check if x is right-truncatable prime number
            if is_right_truncatable_prime(x):

                # Add x to the list of prime numbers
                prime_numbers.append(x)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):

    # Check if n is less than 2
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of n, it is prime
    return True

# Define a function to check if a number is right-truncatable prime
def is_right_truncatable_prime(n):

    # Check if n is prime
    if not is_prime(n):
        return False

    # Check if the last digit of n is equal to 1 or 3
    if n % 10 == 1 or n % 10 == 3:

        # Check if the number formed by removing the last digit from n is prime
        if is_prime(n // 10):
            return True

    # If none of the above conditions are met, the number is not right-truncatable prime
    return False
