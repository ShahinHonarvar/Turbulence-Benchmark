
def prime_factors(my_list):
    return set(reduce(mul, ([p**k for p in prime_factors(n)] for n in my_list), 1))
