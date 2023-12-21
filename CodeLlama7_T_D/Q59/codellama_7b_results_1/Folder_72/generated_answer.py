
def all_left_truncatable_prime(tuple):
    # Initialize list of prime numbers
    prime_numbers = []

    # Loop through the tuple elements
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the prime number to the list
            prime_numbers.append(element)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n-1
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # Return False if there is a factor other than 1 and itself
                return False

    # If n is greater than 1, return True
    return True
