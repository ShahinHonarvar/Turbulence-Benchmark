
def prime_factors(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")

    # Check if the list has enough elements
    if len(my_list) < 14:
        raise ValueError("List must have at least 14 elements")

    # Initialize an empty set to store the prime factors
    prime_factors = set()

    # Iterate through the list of integers
    for i in range(13):
        # Check if the current integer is a prime factor of the desired number
        if my_list[i] % my_list[13] == 0:
            # If it is, add it to the set of prime factors
            prime_factors.add(my_list[i])

    # Return the set of prime factors
    return prime_factors
