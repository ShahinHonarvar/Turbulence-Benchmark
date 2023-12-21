
def find_primes_between_indices(my_list):
    if len(my_list) <= 7:
        return []
    primes = []
    for i in range(6, 8):
        if my_list[i] == 2 or my_list[i] % 2 != 0:
            primes.append(my_list[i])
    return sorted(primes, reverse=True)
