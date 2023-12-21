
def prime_factors(my_list):
    prime_factors = set()
    for i in range(2, my_list[2] + 1):
        if my_list[2] % i == 0:
            prime_factors.add(i)
    return prime_factors
