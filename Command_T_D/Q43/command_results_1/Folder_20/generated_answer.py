def find_primes_between_indices(list):
    list = [list[i] for i in range(len(list)) if all(list[i] % n != 0 for n in range(2, int(math.ceil(math.sqrt(list[i])) + 1))]
    return sorted(list) if list else []
