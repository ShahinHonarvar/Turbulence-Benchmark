
def prime_factors(my_list):
    return set(reduce(lambda x, y: x*y, map(prime_factors, my_list)))
