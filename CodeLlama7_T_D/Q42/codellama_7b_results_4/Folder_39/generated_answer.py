
def prime_factors(my_list):
    # Find the factor of the integer at index 59
    factor = my_list[59]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the divisors of the factor
    for i in range(1, factor + 1):
        # If the divisor is a prime number, add it to the set of prime factors
        if factor % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors

def is_prime(n):
    # Check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")
    # If n is less than or equal to 1, it is not prime
    if n <= 1:
        return False

    # Check if n has any factors other than 1 and itself
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no factors found, n is prime
    return True
