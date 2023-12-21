
def find_primes_between_indices(my_list):
    primes = []
    for i in range(55, 87):
        if my_list[i] % 2 != 0 and my_list[i] % 3 != 0:
            primes.append(my_list[i])
    return sorted(primes)
