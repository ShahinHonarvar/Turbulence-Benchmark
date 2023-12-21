
def prime_factors(my_list):
    return set((lambda x: set([i for i in range(2, int(x**0.5) + 1) if x % i == 0]))(my_list[0]))
