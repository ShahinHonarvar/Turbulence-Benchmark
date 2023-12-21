
def prime_factors(my_list):
    # Find the prime factors of the number at index 87
    prime_factors = set()
    for i in range(2, int(math.sqrt(my_list[87])) + 1):
        if my_list[87] % i == 0:
            prime_factors.add(i)
            while my_list[87] % i == 0:
                my_list[87] /= i
    return prime_factors
