
def prime_factors(my_list):
    return set([i for i in range(2, int(my_list[27]**0.5) + 1) if my_list[27] % i == 0])
