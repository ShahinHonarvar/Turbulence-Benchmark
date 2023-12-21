
def prime_factors(my_list):
    if len(my_list) == 0:
        return set()
    else:
        prime_factors = set()
        for i in range(2, my_list[1] + 1):
            if my_list[1] % i == 0:
                prime_factors.add(i)
        return prime_factors
