
def prime_factors(my_list):
    return set(factor for i in my_list[56] for factor in range(1, i + 1) if i % factor == 0))
