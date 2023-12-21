
def prime_factors(my_list):
    # Find the integer at index 35 in the list
    target_index = 35
    if target_index >= len(my_list):
        raise ValueError("Target index is out of range")
    target_value = my_list[target_index]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the divisors of the target value
    for i in range(1, int(target_value ** 0.5) + 1):
        if target_value % i == 0:
            # If the current divisor is prime, add it to the set of prime factors
            if is_prime(i):
                prime_factors.add(i)
            # Otherwise, recursively find the prime factors of the current divisor and add them to the set of prime factors
            else:
                prime_factors = prime_factors | prime_factors(my_list[target_index // i]])
    return prime_factors
