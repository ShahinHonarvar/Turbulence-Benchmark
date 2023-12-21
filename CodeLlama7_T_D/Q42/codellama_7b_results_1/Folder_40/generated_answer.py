
def prime_factors(my_list):
    # Calculate the prime factors of the integer at index 7
    prime_factors = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            continue

        for j in range(2, int(my_list[i]) ** 0.5 + 1):
            if my_list[i] % j == 0:
                prime_factors.append(j)
                break

    return set(prime_factors)
