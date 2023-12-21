
def prime_factors(my_list):
    return set([prime_factor for i in range(len(my_list)) if my_list[i] % prime_factor == 0])
