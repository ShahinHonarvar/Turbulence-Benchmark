
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple
    for number in tuple:
        # Check if the number is a prime number
        if is_prime(number):
            # If it is, add it to the list of prime numbers
            prime_numbers.append(number)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the number is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True
