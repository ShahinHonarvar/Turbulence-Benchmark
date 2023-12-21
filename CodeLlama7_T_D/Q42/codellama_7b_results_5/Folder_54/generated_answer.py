
def prime_factors(my_list):
    # Find the integer at index 51 in the list
    target_int = my_list[51]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the target integer
    for i in range(2, int(target_int ** 0.5) + 1):
        # If the current number is a factor of the target integer, add it to the prime factors set
        if target_int % i == 0:
            prime_factors.add(i)
    return prime_factors
