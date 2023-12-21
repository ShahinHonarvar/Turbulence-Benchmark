
def prime_factors(my_list):
    # Find the prime factorization of the integer at index 714
    result = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(math.sqrt(my_list[i])) + 1)):
            if my_list[i] % j == 0:
                result.append(j)
                break

    return set(result)
