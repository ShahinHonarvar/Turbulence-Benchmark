
def prime_factors(my_list):
    # Find the prime factor of the integer at index 8
    prime_factor = my_list[8]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the divisors of the prime factor
    for i in range(2, int(prime_factor ** 0.5) + 1):
        # If the current number is a divisor of the prime factor, add it to the set of prime factors
        if prime_factor % i == 0:
            prime_factors.add(i)
    return prime_factors
