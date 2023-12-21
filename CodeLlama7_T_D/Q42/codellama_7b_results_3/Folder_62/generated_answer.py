
def prime_factors(my_list):
    # Find the prime factors of the integer at index 926
    prime_factor = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i] ** 0.5) + 1):
            if my_list[i] % j == 0:
                prime_factor.append(j)
                break

        else:

            prime_factor.append(my_list[i])

    return set(prime_factor)
