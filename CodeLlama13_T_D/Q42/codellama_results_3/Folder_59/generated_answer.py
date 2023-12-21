
def prime_factors(my_list):
    return set([i for i in range(3, my_list[2], 1) if my_list[2] % i == 0])
