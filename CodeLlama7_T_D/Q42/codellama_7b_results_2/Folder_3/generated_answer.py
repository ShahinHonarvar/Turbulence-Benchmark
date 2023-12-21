
def prime_factors(my_list):
    # find the prime factorization of the integer at index 100
    prime_factorization = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        else:

            for j in range(2, int(my_list[i]) + 1):
                if my_list[i] % j == 0:
                    prime_factorization.append(j)
                    break

            else:

                prime_factorization.append(my_list[i])

    return set(prime_factorization)
