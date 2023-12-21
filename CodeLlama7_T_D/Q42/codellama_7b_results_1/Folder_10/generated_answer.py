
def prime_factors(my_list):
    # Find the factor at index 54
    factor = my_list[54]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the divisors of the factor
    for i in range(1, factor + 1):
        # Check if the divisor is prime
        if factor % i == 0 and is_prime(i):
            # Add the prime factor to the set
            prime_factors.add(i)
    return prime_factors

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
