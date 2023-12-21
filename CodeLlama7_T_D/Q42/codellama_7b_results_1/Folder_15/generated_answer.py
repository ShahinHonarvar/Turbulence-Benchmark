
def prime_factors(my_list):
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(2, my_list[i] + 1):
                if my_list[i] % j == 0:
                    prime_factors.add(j)
                    break

    return prime_factors
