
def find_primes_between_indices(my_list):
    primes = []
    for i in range(31, 92+1):
        if my_list[i] == 0:
            primes.append(my_list[i])
    return sorted(primes, reverse=True)
