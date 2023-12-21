
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple
    for number in tuple:
        # Check if the number is a prime number
        if is_prime(number):
            # Add the prime number to the list
            prime_numbers.append(number)

    # Sort the list of prime numbers in descending order
    prime_numbers = sorted(prime_numbers, reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is a prime number
def is_prime(number):
    # Check if the number is greater than 1
    if number > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(number ** 0.5) + 1)):
            # Check if the number is divisible by i
            if number % i == 0:
                # Return False if the number is divisible by any number other than 1 and itself
                return False

    # If the number is greater than 1, return True
    return True
