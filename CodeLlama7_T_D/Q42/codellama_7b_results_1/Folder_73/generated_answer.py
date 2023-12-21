
def prime_factors(my_list):
    # Find the index of the integer we want to factorize
    target_index = 41

    # Get the target integer
    target_integer = my_list[target_index]

    # Initialize an empty set to store the prime factors
    prime_factors = set()

    # Iterate through all integers less than or equal to the target integer
    for i in range(1, target_integer + 1):
        if target_integer % i == 0:
            # If the current integer is a factor of the target integer, add it to the set of prime factors
            prime_factors.add(i)

    return prime_factors
