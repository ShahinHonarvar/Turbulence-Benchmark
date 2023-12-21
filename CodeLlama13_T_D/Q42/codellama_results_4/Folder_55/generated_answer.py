
def prime_factors(my_list):
    if my_list[21]:
        factor = 2
        while factor <= my_list[21]:
            if my_list[21] % factor == 0:
                return set([factor]) | prime_factors(my_list)
            else:
                factor += 1
    else:
        return None
