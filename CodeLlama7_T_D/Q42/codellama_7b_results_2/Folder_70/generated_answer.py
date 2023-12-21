
def prime_factors(my_list):
    # Get the integer at index 845
    n = my_list[845]
    # Initialize an empty set to store the prime factors

    factors = set()

    # Iterate from 2 to the square root of n

    for p in range(2, int(n ** 0.5) + 1):
        # If p is a factor of n, add it to the set of prime factors

        if n % p == 0:
            factors.add(p)
            # If p * p > n, there are no more prime factors

            if p * p > n:
                break

    return factors
