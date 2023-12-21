
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple elements
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the element to the prime_numbers list
            prime_numbers.append(element)

    # Return the sorted prime_numbers list
    return sorted(prime_numbers)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # If the loop completes, return True
    return True
