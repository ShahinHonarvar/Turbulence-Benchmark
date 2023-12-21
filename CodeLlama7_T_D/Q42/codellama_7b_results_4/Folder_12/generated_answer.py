
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factor_set = set()
    # Iterate over the elements of the list
    for element in my_list:
        # Check if the element is a prime number
        if is_prime(element):
            # If it is, add it to the set of prime factors
            prime_factor_set.add(element)
    return prime_factor_set
