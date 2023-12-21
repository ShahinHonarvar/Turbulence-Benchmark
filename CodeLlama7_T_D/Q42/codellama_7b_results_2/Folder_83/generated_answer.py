
def prime_factors(my_list):
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate over the list of integers
    for i in my_list:
        # Check if the integer is a prime number
        if is_prime(i):
            # If it is, add it to the set of prime factors
            prime_factors.add(i)
        # Otherwise, check if the integer can be divided by a prime factor
        else:
            # If it can, add the prime factor to the set of prime factors
            for prime in prime_factors:
                if i % prime == 0:
                    prime_factors.add(prime)
                    break
    return prime_factors
