
def prime_factors(my_list):
    return set(filter(lambda x: x > 1, [i for i in range(2, my_list[49]) if all(my_list[49] % i == 0)]))
