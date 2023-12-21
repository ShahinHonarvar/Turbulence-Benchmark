
def prime_factors(my_list):
    # Get the integer at index 27
    target_int = my_list[27]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through all the numbers less than or equal to the target integer
    for i in range(2, target_int + 1):
        # If the number is divisible by the current number, add it to the set of prime factors
        if target_int % i == 0:
            prime_factors.add(i)
    return prime_factors
