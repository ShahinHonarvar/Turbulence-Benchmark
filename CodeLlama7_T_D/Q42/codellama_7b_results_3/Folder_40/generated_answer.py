
def prime_factors(my_list):
    return set(factor for i in my_list if i == my_list[7] for factor in range(2, int(i ** 0.5) + 1) if i % factor == 0))
