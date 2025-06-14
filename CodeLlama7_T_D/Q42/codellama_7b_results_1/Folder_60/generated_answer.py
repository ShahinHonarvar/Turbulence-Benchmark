
def prime_factors(my_list):
    # Get the number at index 88 in the list
    num = my_list[88]
    # Initialize an empty set to store prime factors
    prime_factor_set = set()
    # Iterate through the divisors of the number
    for i in range(1, int(num ** 0.5) + 1):
        # Check if the current divisor is a prime factor
        if num % i == 0:
            # Add the prime factor to the set
            prime_factor_set.add(i)
    return prime_factor_set
