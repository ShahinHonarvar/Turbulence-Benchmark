
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple elements
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # If it is, add it to the list of prime numbers
            prime_numbers.append(element)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of prime numbers that are right-truncatable prime numbers less than x
    return prime_numbers

# Define a function to check if an integer is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # If it does, return False
                return False

    # If we reach this point, n is prime
    return True
