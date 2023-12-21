
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the elements in the list
    for element in my_list:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the prime factor to the set
            prime_factors.add(element)
    return prime_factors

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If it does, return False
                return False

    # If we reach this point, all tests failed, so n is prime
    return True
