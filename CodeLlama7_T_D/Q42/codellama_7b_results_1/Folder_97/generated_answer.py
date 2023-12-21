
def prime_factors(my_list):
    # Find the prime factorization of the number at index 132
    prime_factors = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(i, len(my_list)):
            if my_list[j] % my_list[i] == 0:
                prime_factors.add(my_list[i])
    return prime_factors
