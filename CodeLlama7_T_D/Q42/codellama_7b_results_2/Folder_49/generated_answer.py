
def prime_factors(my_list):
    # Find the index of the element we want to factorize
    target_index = 68
    # Check if the target index is out of bounds
    if target_index >= len(my_list) or target_index < 0:
        raise ValueError("Target index is out of bounds")
    # Get the target element to factorize
    target_element = my_list[target_index]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the divisors of the target element
    for i in range(1, target_element + 1):
        # Check if the current divisor is prime
        if is_prime(i):
            # Add the prime factor to the set
            prime_factors.add(i)
    return prime_factors
