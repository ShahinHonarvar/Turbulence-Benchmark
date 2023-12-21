
def prime_factors(my_list):
    # Find the prime factors of the number at index 222
    prime_factor = []
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]) + 1):
                if my_list[i] % j == 0:
                    prime_factor.append(j)
    return set(prime_factor)
