
def all_left_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple of integers
    for integer in tuple_of_integers:
        # If the integer is a prime number, add it to the list of prime numbers
        if is_prime(integer):
            prime_numbers.append(integer)

    # Sort the list of prime numbers in descending order and return it
    return sorted(prime_numbers, reverse=True)

# Define a function that checks if an integer is a prime number or not
def is_prime(n):
    # If n is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the loop completes successfully, it means that n is a prime number
    return True
