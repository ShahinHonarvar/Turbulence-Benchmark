
def prime_factors(my_list):
    # Get the integer at index 828
    n = my_list[828]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of n
    for p in range(2, int(n ** 0.5) + 1):
        # If p is a factor of n, add it to the set of prime factors
        if n % p == 0:
            prime_factors.add(p)
    return prime_factors
