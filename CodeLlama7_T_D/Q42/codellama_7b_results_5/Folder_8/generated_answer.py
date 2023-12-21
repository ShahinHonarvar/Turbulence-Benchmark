
def prime_factors(my_list):
    # Find the number at index 49
    number = my_list[49]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all divisors of the number
    for i in range(1, number + 1):
        # If the current divisor is a prime factor of the number
        if number % i == 0 and is_prime(i):
            # Add the prime factor to the set of prime factors
            prime_factors.add(i)
    return prime_factors

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
