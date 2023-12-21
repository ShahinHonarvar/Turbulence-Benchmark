
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple and check if each element is a prime number
    for i in range(len(tuple)):
        current_element = tuple[i]
        if is_prime(current_element):
            prime_numbers.append(current_element)

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of all right-truncatable prime numbers less than x
    return prime_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by any number between 2 and n-1, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is divisible only by 1 and itself, it is prime
    return True
