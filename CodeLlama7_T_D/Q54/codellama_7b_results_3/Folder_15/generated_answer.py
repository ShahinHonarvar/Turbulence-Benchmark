
def all_right_truncatable_prime(n):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the numbers less than n
    for i in range(2, n):
        # Check if the number is prime
        if is_prime(i):
            # Add the prime number to the list
            prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, n is prime
    return True
