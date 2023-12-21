
def prime_factors(my_list):
    # Find the prime factorization of the integer at index 45
    prime_factorization = set()
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i]) ** 0.5 + 1):
            if my_list[i] % j == 0:
                prime_factorization.add(j)
                break

    return prime_factorization
