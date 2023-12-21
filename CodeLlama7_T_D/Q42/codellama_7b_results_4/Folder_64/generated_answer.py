
def prime_factors(my_list):
    if len(my_list) == 0:
        return set()
    else:
        prime_factor = my_list[1]
        for i in range(2, int(prime_factor ** 0.5) + 1):
            while prime_factor % i == 0:
                prime_factor /= i

        return set([prime_factor]) | prime_factors(my_list[1:])
