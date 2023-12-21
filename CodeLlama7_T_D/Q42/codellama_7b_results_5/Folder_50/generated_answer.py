
def prime_factors(my_list):
    # Find the prime factor of the element at index 40
    prime_factor = my_list[40]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the divisors of the prime factor
    for i in range(1, prime_factor + 1):
        # If the current divisor is a prime number and it divides the prime factor without leaving a remainder, add it to the set of prime factors
        if i > 1 and prime_factor % i == 0:
            prime_factors.add(i)
    return prime_factors
