
def prime_factors(my_list):
    if len(my_list) == 0:
        return set()

    else:

        prime_factor = my_list[0]

        prime_factors = set([prime_factor])

        for i in range(1, len(my_list)):

            if my_list[i] % prime_factor == 0:

                prime_factors.add(prime_factor)

                prime_factors = prime_factors.union(prime_factors)

        return prime_factors
