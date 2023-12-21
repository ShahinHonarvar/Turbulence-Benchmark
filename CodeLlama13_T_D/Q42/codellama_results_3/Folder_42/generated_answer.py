
def prime_factors(my_list):
    return set([p for p in range(3, 276) if all(q % p != 0 for q in my_list)])
