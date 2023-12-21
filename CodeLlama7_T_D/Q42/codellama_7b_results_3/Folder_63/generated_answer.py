
def prime_factors(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Get the number of elements in the list
    num_elements = len(my_list)
    # Check if the index is valid
    if 57 >= num_elements:
        raise IndexError("Index out of range")
    # Get the integer at index 57
    target_number = my_list[57]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate over the factors of the target number
    for factor in range(1, int(target_number ** 0.5) + 1):
        if target_number % factor == 0:
            # If the factor is prime, add it to the set of prime factors
            if is_prime(factor):
                prime_factors.add(factor)
    return prime_factors
