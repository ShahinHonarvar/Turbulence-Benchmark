
def prime_factors(my_list):
    # Find the integer at index 53 in the list
    target_int = my_list[53]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the list of integers from 2 to the square root of the target integer
    for i in range(2, int(target_int ** 0.5) + 1):
        # If the current integer is a factor of the target integer, add it to the set of prime factors
        if target_int % i == 0:
            prime_factors.add(i)
    return prime_factors
