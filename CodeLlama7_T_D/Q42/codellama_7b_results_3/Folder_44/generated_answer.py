
def prime_factors(my_list):
    # Find the prime factorization of the integer at index 828
    prime_factorization = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        else:

            while my_list[i] % 2 == 0:
                my_list[i] /= 2

            for j in range(3, int(my_list[i]) ** 0.5 + 1, 2):
                if my_list[i] % j == 0:
                    prime_factorization.append(j)
                    while my_list[i] % j == 0:
                        my_list[i] /= j

            prime_factorization.append(my_list[i])

    return set(prime_factorization)
