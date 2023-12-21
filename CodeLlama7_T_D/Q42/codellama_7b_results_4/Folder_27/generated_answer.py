
def prime_factors(my_list):
    # Find the integer at index 56
    target_index = 56
    # Check if the target index is within bounds
    if target_index >= len(my_list) or target_index < 0:
        raise ValueError("Target index out of bounds")
    # Get the target integer
    target_int = my_list[target_index]
    # Find all prime factors of the target integer
    prime_factors = []
    for i in range(2, int(target_int ** 0.5) + 1):
        if target_int % i == 0:
            prime_factors.append(i)
    return set(prime_factors)
