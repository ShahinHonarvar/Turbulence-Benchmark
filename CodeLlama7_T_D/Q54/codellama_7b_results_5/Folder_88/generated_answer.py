
def all_right_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for i in range(len(tuple)):
        # Assign the current integer to a variable
        current_integer = tuple[i]

        # Check if the current integer is a prime number
        if is_prime(current_integer):
            # If the current integer is a prime number, add it to the list of prime numbers
            prime_numbers.append(current_integer)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers
    return prime_numbers

# Define a function to check if an integer is a prime number
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        # If n is less than 2, it is not a prime number
        return False

    # Loop through the numbers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if n is divisible by i
        if n % i == 0:
            # If n is divisible by i, it is not a prime number
            return False

    # If the loop completes without finding any divisors of n, n is a prime number
    return True
