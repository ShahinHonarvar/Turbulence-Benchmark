
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the elements of the list
    for element in my_list:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the prime factor to the set
            prime_factors.add(element)
    # Return the set of prime factors
    return prime_factors

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, n is prime
    return True
