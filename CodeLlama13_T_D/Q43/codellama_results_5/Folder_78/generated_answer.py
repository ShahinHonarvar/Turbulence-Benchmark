
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(28, 84):
        if my_list[i] % 2 == 0 and my_list[i] != 2:
            continue
        for j in range(3, int(my_list[i] ** 0.5) + 1, 2):
            if my_list[i] % j == 0:
                break
        else:
            prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
