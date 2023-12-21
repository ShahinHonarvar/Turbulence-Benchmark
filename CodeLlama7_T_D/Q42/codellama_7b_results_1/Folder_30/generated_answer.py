
def prime_factors(my_list):
    # Find the factor of the element at index 94
    factor = my_list[94]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through the list of integers and find the prime factors of the element at index 94
    for i in range(len(my_list)):
        if my_list[i] % factor == 0:
            prime_factors.add(factor)
    return prime_factors
