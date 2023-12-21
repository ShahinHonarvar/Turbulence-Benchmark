
def prime_factors(my_list):
    return {p: my_list[85] for p in set(map(lambda x: x[0], filter(lambda x: x[1] > 1, map(lambda y: (y, y % y), range(2, int(sqrt(my_list[85])) + 1))))))}
