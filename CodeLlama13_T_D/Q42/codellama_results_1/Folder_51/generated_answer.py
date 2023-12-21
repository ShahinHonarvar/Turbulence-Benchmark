
def prime_factors(list_of_ints):
    return {factor for factor in range(1, list_of_ints[64] + 1) if list_of_ints[64] % factor == 0 and is_prime(factor)}
