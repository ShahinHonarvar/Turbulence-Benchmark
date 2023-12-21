
def prime_factors(my_list):
    # Find the prime factor of the number at index 4
    prime_factor = 2
    while my_list[4] % prime_factor != 0:
        prime_factor += 1
    return {prime_factor}
