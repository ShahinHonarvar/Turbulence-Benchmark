
def prime_factors(my_list):
    # Find the prime factor of the integer at index 6
    prime_factor = my_list[6]
    # Create an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the numbers less than or equal to the prime factor
    for i in range(2, prime_factor + 1):
        # If the number is a factor of the prime factor, add it to the set of prime factors
        if prime_factor % i == 0:
            prime_factors.add(i)
    return prime_factors
