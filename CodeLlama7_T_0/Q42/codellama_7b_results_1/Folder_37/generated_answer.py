
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the list of integers
    for i in my_list:
        # Check if the integer is a prime number
        if is_prime(i):
            # If it is, add it to the set of prime factors
            prime_factors.add(i)
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

    # If we reach this point, either n is a prime number or n is 1
    return True
