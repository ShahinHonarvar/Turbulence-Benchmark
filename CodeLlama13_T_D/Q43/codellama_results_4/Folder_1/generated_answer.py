
def find_primes_between_indices(my_list):
    primes = []
    for i in range(87, 90):
        if my_list[i] in [2, 3, 5, 7]:
            primes.append(my_list[i])
    return sorted(primes)
