
def prime_factors(my_list):
    # Find the prime factors of the integer at index 93
    prime_factor = []
    for i in range(len(my_list)):
        if my_list[i] == 1:
            prime_factor.append(my_list[i])
        else:
            while my_list[i] % 2 == 0:
                my_list[i] = my_list[i] // 2
            while my_list[i] % 3 == 0:
                my_list[i] = my_list[i] // 3
            while my_list[i] % 5 == 0:
                my_list[i] = my_list[i] // 5
            prime_factor.append(my_list[i])
    return set(prime_factor)
