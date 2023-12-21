
def prime_factors(my_list):
    # Find the prime factorization of the number at index 790
    prime_factorization = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i]) + 1):
            if my_list[i] % j == 0:
                prime_factorization.append(j)
                break

    return set(prime_factorization)
