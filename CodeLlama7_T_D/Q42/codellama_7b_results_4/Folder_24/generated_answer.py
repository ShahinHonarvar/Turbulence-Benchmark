
def prime_factors(my_list):
    # Find the prime factor of the number at index 74
    prime_factor = 2
    while my_list[74] > 1:
        if my_list[74] % prime_factor == 0:
            my_list[74] /= prime_factor
        else:
            prime_factor += 1

    # Return the set of all prime factors
    return {prime_factor}
