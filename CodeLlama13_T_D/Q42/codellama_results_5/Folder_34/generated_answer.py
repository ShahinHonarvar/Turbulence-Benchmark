
def prime_factors(my_list):
    return set([i for i in range(2, my_list[97]+1) if all(my_list[97] % i != 0 for j in range(2, int(math.sqrt(my_list[97]))+1))])
