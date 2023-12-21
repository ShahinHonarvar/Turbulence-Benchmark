
def prime_factors(my_list):
    # Find the prime factorization of the number at index 77
    prime_factors = set()
    for i in range(2, int(my_list[77]) + 1):
        if my_list[77] % i == 0:
            prime_factors.add(i)
    return prime_factors
