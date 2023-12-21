
def prime_factors(my_list):
    # Find the prime factors of the integer at index 194
    prime_factor = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            prime_factor.append(i)
    return set(prime_factor)
