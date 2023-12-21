
def prime_factors(my_list):
    return set([x for x in range(2, my_list[35]) if my_list[35] % x == 0 and all([y % x != 0 for y in range(2, int(my_list[35] ** 0.5) + 1)])])
