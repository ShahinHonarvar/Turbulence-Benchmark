
def find_primes_between_indices(my_list):
    primes = []
    for i in range(23, 40):
        if my_list[i] == 1:
            primes.append(my_list[i])
    return sorted(primes)
