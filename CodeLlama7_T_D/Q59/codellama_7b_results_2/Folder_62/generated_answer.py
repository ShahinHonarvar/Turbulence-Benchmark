
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through the tuple and check if each element is a prime number
    for element in tuple:
        if is_prime(element):
            prime_numbers.append(element)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the list of prime numbers
    return prime_numbers

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no number between 2 and sqrt(n) divides n, then it is prime
    return True
